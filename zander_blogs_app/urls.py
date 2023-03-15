"""
    Defines URL patterns for the zander_blogs_app
    This is defined by me
"""

from django.urls import path

from . import views # the dot means to import the views.py module from the
                    # same directory

app_name = "zander_blogs_app"

# List of individual pages that can be requested from the app
urlpatterns = [
    # Home Page
    path("", views.homePage, name="homepage"),

    # The page that will list the blogs
    path("blogs/", views.blogList, name="bloglist"),

    # Each blog's content
    path("blogs/<int:blogcontent_id>/", views.blogContent, name="blogcontent"),
]