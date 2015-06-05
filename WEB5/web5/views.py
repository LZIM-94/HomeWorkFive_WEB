from pyramid.view import view_config



@view_config(route_name='home', renderer='templates/home.jinja2')
def index(request):
    return {'link': '<a href="about/aboutme.html">GET INFO ABOUT ME</a>'}


@view_config(route_name='about', renderer='templates/about/aboutme.jinja2')
def about(request):
    return {'link': '<a href="/">GO TO HOME PAGE</a>'}
