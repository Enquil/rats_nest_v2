from django.db import models


@admin.register(Domain)
class Domain(models.Model):

    class Meta:
        verbose_name_plural = 'Domains'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


@admin.register(Category)
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    parent = models.ForeignKey(self,
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    M_OR_F = (
            ("0", "unisex"),
            ("1", "male"),
            ("2", "female"),
    )

    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254,
                           null=True,
                           blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254)
    description = models.TextField()
    feature_list = models.CharField()
    m_or_f = models.Choicefield(M_OR_F, default=0)
    has_sizes = models.BooleanField(default=False,
                                    null=True,
                                    blank=True,)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024,
                                null=True,
                                blank=True)
    image = models.ImageField(null=True,
                              blank=True)

    def __str__(self):
        return self.name
