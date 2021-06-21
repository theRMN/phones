from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.TextField()
    image = models.TextField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name} | {self.image} | {self.price} | {self.release_date} | {self.lte_exists} | {self.slug}'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)


