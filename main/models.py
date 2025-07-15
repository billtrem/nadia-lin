from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# -------------------------
# Homepage Content
# -------------------------

class HomepageImage(models.Model):
    image = CloudinaryField('image')  # ✅ Cloudinary
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or "Homepage Image"

    class Meta:
        verbose_name = "Homepage Carousel Image"
        verbose_name_plural = "Homepage Carousel Images"

# -------------------------
# Info Page (bio + portrait + optional contact)
# -------------------------

class InfoPageContent(models.Model):
    portrait = CloudinaryField('image', blank=True, null=True)  # ✅ Cloudinary
    bio = models.TextField(help_text="Nadia-Lin’s bio or artist statement")
    contact_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "Info Page Content"

    class Meta:
        verbose_name = "Info Page Content"
        verbose_name_plural = "Info Page Content"

# -------------------------
# Blog
# -------------------------

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)  # auto-generated if blank
    body = models.TextField()
    preview_image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

# -------------------------
# Exhibitions
# -------------------------

class Exhibition(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('current', 'Current'),
        ('past', 'Past'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    image = CloudinaryField('image', blank=True, null=True)  # ✅ Cloudinary

    def __str__(self):
        return f"{self.title} ({self.status})"

# -------------------------
# Shop / Products
# -------------------------

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')  # ✅ Cloudinary
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sumup_link = models.URLField(help_text="Paste the SumUp payment link here")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
