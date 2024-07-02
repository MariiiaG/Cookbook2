from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50,
                            help_text=" Enter the category of your Recipe",
                            verbose_name="Recipe Category")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20,
                                  help_text="Enter your first name",
                                  verbose_name="Your first name")
    last_name = models.CharField(max_length=30,
                                 help_text="Enter your last name",
                                 verbose_name="Your last name")
    objects: models.Manager()

    def __str__(self):
        return self.last_name


class Recipe(models.Model):
    title = models.CharField(max_length=50,
                             help_text="Enter the title",
                             verbose_name="Recipe title")
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 help_text="Enter the recipe category",
                                 verbose_name="Recipe category",
                                 null=True)
    cooking_time = models.DecimalField(decimal_places=1,
                                       max_digits=3,
                                       help_text="Enter estimated cooking time",
                                       verbose_name="Cooking time (in mins)")
    author = models.ManyToManyField('Author',
                                    help_text="Enter the author(s) of the recipe",
                                    verbose_name="Recipe author(s)")
    description = models.TextField(max_length=150,
                                   help_text="Provide the quick description",
                                   verbose_name="Recipe description")
    cooking_method = models.TextField(max_length=1000,
                                      help_text="Describe the cooking process",
                                      verbose_name="Recipe description")
    photo = models.ImageField(upload_to='images',
                              help_text="Upload a photo",
                              verbose_name="Photo", null=True)

    objects: models.Manager()

    def display_author(self):
        return ', '.join([author.last_name for author in
                          self.author.all()])
    display_author.short_description = "Authors"


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])

