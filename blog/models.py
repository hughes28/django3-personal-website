from django.db import models

# Create models of components to be added to admin.
# List everything in the class that you want to add.
# In this case, it is a title, description, image, and a URL.

class Post(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	description = models.TextField()

	def __str__(self):
		return self.title # shows name of post in admin