from django.db import models
from django.template.defaultfilters import slugify

class Carlist(models.Model):
    carimage = models.ImageField(default='default/no_image.jpg', blank=True, null=True, upload_to='images',max_length=125)
    brand = models.CharField(max_length=100)
    carname = models.CharField(max_length=100,null=True)
    price = models.FloatField()
    slug = models.SlugField(default="", blank=True, null=True)

    def __str__(self):
        return self.carname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand + "-" + str(self.carname))
        return super().save(*args, **kwargs)


class Trip(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car = models.ForeignKey(Carlist, on_delete=models.CASCADE, null=True, related_name='car')
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    pick_up = models.CharField(max_length=100)
    drop_off = models.CharField(max_length=100)
    pick_date = models.CharField(max_length=100)
    drop_date = models.CharField(max_length=100)
    time_pick = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subjects = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name