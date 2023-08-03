from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        MOD = "MOD", 'Mod'
        PROFESSIONAL = "PROFESSIONAL", 'Professional'
        ADVANCED = "ADVANCED", 'Advanced'
        NEWBIE = "NEWBIE", 'Newbie'
        
    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices= Role.choices, )
    
    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True,)
    hidden = models.BooleanField(default=False)
    user = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/',)

    def __str__(self):
        return self.post.title



# likes
# follow
# add to collection
# followed by
# dislikes
# post as individual
# giing credits

# Team/clan/guild
# -> profession level
# -> like dislike ratio
# post as guild

# events
# beeing able to join
