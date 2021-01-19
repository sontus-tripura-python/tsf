from django.db import models

# Create your models here.
class TsfAboutSetting(models.Model):
    tsf_logo = models.ImageField(upload_to='tsf_logo', blank=True)
    tsf_greeting = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    tsf_phone = models.CharField(max_length=255, blank=True)
    tsf_email = models.EmailField(max_length=255, blank=True)
    tsf_address = models.TextField(blank=True)
    tsf_about = models.TextField(blank=True)
    tsf_president_name = models.CharField(max_length=255, blank=True)
    tsf_president_photo = models.ImageField(upload_to='president_photo', blank=True)
    tsf_president_title = models.CharField(max_length=255, blank=True)
    tsf_secretary_name = models.CharField(max_length=255, blank=True)
    tsf_secretary_photo = models.ImageField(upload_to='secretary_photo', blank=True)
    tsf_secretary_title = models.CharField(max_length=255, blank=True)
    tsf_fb_link = models.URLField(max_length=255, blank=True)
    tsf_twitter_link = models.URLField(max_length=255, blank=True)
    tsf_instagram_link = models.URLField(max_length=255, blank=True)
    tsf_linkdin_link = models.URLField(max_length=255, blank=True)
    tsf_youtube_link = models.URLField(max_length=255, blank=True)
    developer_name = models.CharField(max_length=200)
    developer_address = models.CharField(max_length=250)
    developer_website = models.URLField(blank=True)
    developer_email = models.EmailField(blank=True)
    developer_fb = models.URLField(blank=True)
    developer_youtube = models.URLField(blank=True)
    developer_instagram = models.URLField(blank=True)
    developer_linkdin = models.URLField(blank=True)

    def __str__(self):
        return f"{self.tsf_greeting} of tsf"

    class Meta:
        verbose_name_plural = "TSF ABOUT"

    


class Slider(models.Model):
    title = models.CharField(max_length=200)
    silder_image = models.ImageField(upload_to='slider_img', blank=True)

    def __str__(self):
        return self.title