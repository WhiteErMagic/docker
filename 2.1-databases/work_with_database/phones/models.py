from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='phones_img')
    release_date = models.DateField()
    lte_exists = models.BooleanField()


    def __str__(self):
        return self.name
