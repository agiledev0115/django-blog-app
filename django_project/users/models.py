from django.db import models
from django.contrib.auth.models import User
from PIL import Image

User._meta.get_field('email')._unique = True # unique email

# Create your models here.

# create a new model for profile which in one-to-one to the user
# if user deleted then profile will also deleted but, vice-versa not true
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    ######### how we wanted to printed out profile ############
    # def __str__(self):
    #     return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path) # open the image
    #     if img.height > 300 or img.width > 300: # check height and width of the image
    #         output_size = (300, 300) # define the size of the image
    #         img.thumbnail(output_size) # resize the image
    #         img.save(self.image.path) # save the image in the same path


