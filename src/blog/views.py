from django.conf import settings
from django.shortcuts import render_to_response

from haystack.views import SearchView
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

from blog.models import Tweet, Blog

class Form(SearchForm):

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data['q']:
            return self.no_query_found()

        sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

        if self.load_all:
            sqs = sqs.load_all()

        return sqs


class MySearchView(SearchView):

    def __init__(self, *args, **kwargs):
        kwargs['form_class'] = Form
        super(MySearchView, self).__init__(*args, **kwargs)

    def __call__(self, request):
        self.request = request

        sqs = SearchQuerySet().models(Blog).filter(user=request.user)

        if request.GET.get('date'):
            sqs = sqs.filter(pub_date__gte=request.GET.get('date'))

        self.form = self.build_form(sqs)
        self.query = self.get_query()
        self.results = self.get_results()

        #raise Exception(self.results)
        return self.create_response()

    def build_form(self, sqs, form_kwargs=None):
        """
        Instantiates the form the class should use to process the search query.
        """
        data = None
        kwargs = {
            'load_all': self.load_all,
        }
        if form_kwargs:
            kwargs.update(form_kwargs)

        if len(self.request.GET):
            data = self.request.GET

        kwargs['searchqueryset'] = sqs

        return self.form_class(data, **kwargs)

    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """
        (paginator, page) = self.build_page()

        context = {
            'query': self.query,
            'form': self.form,
            'page': page,
            'paginator': paginator,
            'suggestion': None,
        }

        if getattr(settings, 'HAYSTACK_INCLUDE_SPELLING', False):
            context['suggestion'] = self.form.get_suggestion()

        context.update(self.extra_context())
        return render_to_response(self.template, context, context_instance=self.context_class(self.request))
    