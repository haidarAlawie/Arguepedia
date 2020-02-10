from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
User = settings.AUTH_USER_MODEL

class ArgumentPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)
	def search(self, query):
		lookup = (Q(title__icontains=query) |
		Q(content__icontains=query)|
		Q(user__username__icontains=query)
		)
		return self.filter(title__icontains=query)


class ArgumentPostManager(models.Manager):
	def get_queryset(self):
		return ArgumentPostQuerySet(self.model, using=self._db)
	
	def get_published(self):
		return self.get_queryset().published()

	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		else:
			return self.get_queryset().search(query)






class ArgumentPost(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='image/', blank=True, null=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(null=True)
	content = models.TextField(null=True, blank=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	objects = ArgumentPostManager()

	class Meta:
		ordering = ['-publish_date', '-updated', 'timestamp']

	def get_detail_url(self):
		return f"/arguments/{self.id}/"
	def get_edit_url(self):
		return f"/arguments/{self.id}/edit/"
	def get_delete_url(self):
		return f"/arguments/{self.id}/delete/"
