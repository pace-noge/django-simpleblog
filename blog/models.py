from django.db import models
from django.core.mail import send_mail
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=60)
	body = models.TextField()
	post = models.ForeignKey(Post)

	def save(self, *args, **kwargs):
	    """ email when comment added."""
	    if "notify" in kwargs and kwargs["notify"] == True:
		    message = "Comment was added to '%s' by '%s':\n\n%s" % (self.post, self.author, self.body)
		    from_addr = "no-replay@example.com"
		    recipient_list = ["nasa.freaks@gmail.com"]
		    send_mail("new comment added", message, from_addr, recipient_list)

	    if "notify" in kwargs: del kwargs["notify"]

	    super(Comment, self).save(*args, **kwargs)