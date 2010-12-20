from django import template

register = template.Library()

@register.tag
def get_model_class_matches(parser, token):

    bits = token.split_contents()

    if len(bits) != 5 or bits[3] != "as":
        raise template.TemplateSyntaxError("Must pass 'results model as var' to %s tag" % bits[0])

    return SearchResultNode(bits[1], bits[2], bits[4])

class SearchResultNode(template.Node):

    def __init__(self, results, model_class, var_name):
        self.results = template.Variable(results)
        self.model_class = model_class
        self.var_name = var_name

    def render(self, context):
        matches = []
        for result in self.results.resolve(context):
            if result.model.__name__ == self.model_class:
                matches.append(result)

        #raise Exception(matches)
        context[self.var_name] = matches

        return ''