from django.db import models

# Create models of components to be added to admin.
# List everything in the class that you want to add.
# In this case, it is a title, description, image, and a URL.

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/')
	url = models.URLField(blank=True) # Do not necessarily need it

	def __str__(self):
		return self.title # shows name of project in admin