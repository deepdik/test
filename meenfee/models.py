from django.db import models

CITYNAME = (('amman', 'Amman'), ('irbid', 'Irbid'),('aqaba','Aqaba'))
LEVELSKILLS = (('beginner','Beginner'),('Medium','medium'),('Expert','expert'))
LOCATION = (('I travel to my customers','I travel to my customers'),('Customers travel to me','Customers travel to me'),('Remotely','Remotely'))
DISTANCE = (('5 minutes away','5 minutes away'),('20 minutes away','20 minutes away'),('30 minutes away','30 minutes away'))
UNITS = (('1 hour','1 hour'),('2 hour','2 hour'),('3 hour','3 hour'))
# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=120)
   
    def __str__(self):
        return '%s' % (self.city)

    class Meta:
    
        verbose_name_plural = "Cities"

class Category(models.Model):
    category = models.CharField(max_length=120)
   
    def __str__(self):
        return '%s' % (self.category)

    class Meta:
        verbose_name_plural = "Catagories"

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=120)
    def __str__(self):
        return '%s' % (self.subcategory)

    class Meta:
        verbose_name_plural = "SubCatagories"

        
class ServiceProvider(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    mobileNo = models.CharField(max_length=14)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    subCategory = models.ManyToManyField(SubCategory)
    levelskill = models.CharField(max_length=120, choices=LEVELSKILLS)
    location = models.CharField(max_length=120,choices=LOCATION)
    distance_limit = models.CharField(max_length=100,choices=DISTANCE)
    provide_tools = models.BooleanField(default=True)
    instant_booking = models.BooleanField(default=True)
    bannerImage = models.ImageField(upload_to='static/admin/img',
                                    default = 'static/admin/img/img.jpg'
                                    )
    def __str__(self):
        return '%s' % (self.firstname)

    class Meta:
        verbose_name_plural = "ServiceProviders"

        