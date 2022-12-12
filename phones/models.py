from django.db import models
from django.urls import reverse

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(verbose_name="FOTO")
    release_date = models.CharField(max_length=11)
    lte_exists = models.BooleanField(verbose_name="BOOL")
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    # def get_abs_url(self):
    #     return reverse("any_phone", kwargs={'slug': self.slug})

    # TODO: Добавьте требуемые поля
    # pass
