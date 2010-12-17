from haystack.views import SearchView
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

class MySearchView(SearchView):

    def __init__(self, *args, **kwargs):
        kwargs['form_class'] = SearchForm
        super(MySearchView, self).__init__(*args, **kwargs)

    def __call__(self, request):
        self.request = request

        sqs = SearchQuerySet().filter(user=request.user)
        if request.GET.get('date'):
            sqs = sqs.filter(pub_date__gte=request.GET.get('date'))

        self.form = self.build_form(sqs)
        self.query = self.get_query()
        self.results = self.get_results()
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
