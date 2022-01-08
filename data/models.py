from django.db import models
from django.utils.text import slugify

# Create your models here.


class Our_business(models.Model):
    name = models.CharField(max_length=160)
    sub_name = models.CharField(max_length=160, blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    img = models.ImageField(default='background/default.jpg',
                            upload_to='background/', blank=True)
    about = models.CharField(max_length=160)
    business_category = models.CharField(max_length=160, blank=True, null=True)
    # link of website about pages
    Website = models.URLField(null=True, blank=True)
    # Social media
    FacebookUrl = models.URLField(null=True, blank=True)
    TwitterUrl = models.URLField(null=True, blank=True)
    LinkedInUrl = models.URLField(null=True, blank=True)
    InstragramUrl = models.URLField(null=True, blank=True)

    # contact
    mail_id = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Our_business, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Our_business'
        # Add verbose name
        verbose_name = 'Our_business'


# our products and services
PRODUCT_TYPE = (
    ("Digital Product", "Digital Product"),
    ("Digital Service", "Digital Service"),
    ("Product", "Product"),
    ("Service", "Service"),

)


class Our_products(models.Model):
    name = models.CharField(max_length=160)
    sub_name = models.CharField(max_length=160, blank=True, null=True)
    Brand = models.CharField(max_length=160, blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    img = models.ImageField(default='background/default.jpg',
                            upload_to='background/', blank=True)
    about = models.CharField(max_length=160)
    Company = models.ForeignKey(
        'Our_business', null=True, on_delete=models.CASCADE,)

    Product_category = models.CharField(max_length=160, blank=True, null=True)
    producttype = models.CharField(
        max_length=160,
        choices=PRODUCT_TYPE,
        default='Product',
        null=True, blank=True
    )
    # link of website about pages
    Link = models.URLField(null=True, blank=True)
    # contact
    mail_id = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Our_products, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Our_products'
        # Add verbose name
        verbose_name = 'Our_products'


class Our_Team(models.Model):
    name = models.CharField(max_length=160)
    designation = models.CharField(max_length=160, blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    img = models.ImageField(default='background/default.jpg',
                            upload_to='background/', blank=True)
    about = models.CharField(max_length=160)

    # link of website about pages
    Website = models.URLField(null=True, blank=True)
    # Social media
    FacebookUrl = models.URLField(null=True, blank=True)
    TwitterUrl = models.URLField(null=True, blank=True)
    LinkedInUrl = models.URLField(null=True, blank=True)
    InstragramUrl = models.URLField(null=True, blank=True)

    # contact
    mail_id = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Our_Team, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Our_Team'
        # Add verbose name
        verbose_name = 'Our_Team'
