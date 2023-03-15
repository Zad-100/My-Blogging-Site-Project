from django.shortcuts import render

from .models import Headline, BlogContent

# Create your views here.

# View function for the homepage
def homePage(request):
    """The view function for the homepage of the blogging site"""
    return(render(request, "zander_blogs_app/homepage.html"))
# end homepage view function

# View function for the blog listing page
def blogList(request):
    """Shows all blogs' headlines"""
    headlines = Headline.objects.order_by('dateCreated')
    context = {"blogHeadlines": headlines}

    return(render(request, 'zander_blogs_app/bloglist.html', context))
# end view function blogList

# View function for the blog content
def blogContent(request, blogcontent_id):
    """Show the content of a blog that was clicked"""
    headline = Headline.objects.get(id=blogcontent_id)
    content = headline.blogcontent

    context = {
        "headLine": headline,
        "blogContent": content,
    }

    return(render(request, "zander_blogs_app/blogcontent.html", context))
# end function blogContent