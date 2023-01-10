from django.db import models

# Create your models here.

class Headline(models.Model):
    """This is the heading of the blog describing it"""
    headingName = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the model to used to refer
        to the model when required
        """
        return(self.headingName)
    # end function __str__()
# end class Headline

class BlogContent(models.Model):
    """This is the content of the blog"""
    # OneToOneField default primary_key attribute is False
    # As we do not want the content of the blog to be its primary key
    heading = models.OneToOneField(Headline, on_delete=models.CASCADE)
    content = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representing the content model"""
        if len(self.content) > 50:
            return f"{self.content[: 50]}..."
        else:
            return f"{self.content}"
        # end if-else
    # end funtion __str__()
# end class BlogContent