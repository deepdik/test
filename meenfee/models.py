from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CITYNAME    = (('amman', 'Amman'), ('irbid', 'Irbid'),('aqaba','Aqaba'))
LEVELSKILLS = (('Beginner','Beginner'),('Medium','medium'),('Expert','Expert'))
LOCATION    = (('I travel to my customers','I travel to my customers'),('Customers travel to me','Customers travel to me'),('Remotely','Remotely'))
DISTANCE    = (('5 minutes away','5 minutes away'),('20 minutes away','20 minutes away'),('30 minutes away','30 minutes away'))
UNITS       = (('1 hour','1 hour'),('2 hour','2 hour'),('3 hour','3 hour'))


class City(models.Model):
    city    = models.CharField(max_length=40,unique=True)
   
    def __str__(self):
        return self.city
    class Meta:    
        verbose_name_plural = "Cities"


class Category(models.Model):
    category = models.CharField(max_length=40 ,unique=True)
   
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Catagories"



class SubCategory(models.Model):
    category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=40)
    def __str__(self):
        return self.subcategory
    class Meta:
        verbose_name_plural = "SubCatagories"


        
class Service(models.Model):
    '''
    model for service add by provider
    '''
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    category                = models.ForeignKey(Category, on_delete=models.CASCADE)  
    subcategory             = models.ManyToManyField(SubCategory)
    experience              = models.TextField(blank=True,null=True)
    levelskill              = models.CharField(max_length=120, choices=LEVELSKILLS)
    location                = models.CharField(max_length=120, choices=LOCATION)
    city                    = models.ForeignKey(City,blank=True,on_delete=models.DO_NOTHING)
    distance_limit          = models.CharField(max_length=100, choices=DISTANCE)
    service_pricing         = models.PositiveIntegerField()
    pricing_unit            = models.CharField(max_length=30)
    quote_at_request        = models.BooleanField(default=False, help_text='This will create popup when they accept a requester request')
    provide_tools           = models.BooleanField(default=True)
    tool_specify            = models.TextField(blank =True, null=True)
    instant_booking         = models.BooleanField(default =True)
    profile_img             = models.ImageField(upload_to ='service/img',
                                    default = 'service/img/default.jpg'
                                    )

    # This is for task completed by provider in this service
    completed_task          = models.PositiveIntegerField(default=0)
    avg_rating              = models.FloatField(default=0.0)

    # check it  type of tasker and response time(i think it should be some choices field)
    type_of_tasker          = models.CharField(max_length=15 ,blank=True,null=True)
    response_within         = models.CharField(max_length=15 ,blank=True,null=True)

    # extra fields to apply filter
    profile_views           = models.PositiveIntegerField(default=0)
    created                 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name +'-'+self.category.category

    class Meta:
        verbose_name_plural = "Services"

class ServiceProviderAvailability(models.Model):
    '''
    Service provider can select different-different availability
    time for different date. This model will also be used in Calender feature
    '''
    service                     = models.ForeignKey(Service, on_delete=models.CASCADE)
    availability_date           = models.DateField()
    availability_time_from      = models.TimeField()
    availability_time_to        = models.TimeField()

    def __int__(self):
        return self.service

    class Meta:
        verbose_name_plural = "Service Provider Availability"


class ServiceRating(models.Model):
    '''
    Requester can give Rating  to service provider after service completion
    After rating by requester, provider avg_rating in service model should be
    change and it would be avg of all rating provided by all requester
    '''

    service             = models.ForeignKey(Service, on_delete=models.CASCADE)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    rating              = models.PositiveIntegerField( validators=[MaxValueValidator(5), MinValueValidator(1)])
    created             = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.service) +' - '+str(self.user)+' - '+str(self.rating)


class ServiceFeedback(models.Model):
    '''
    Requester can give Feedback  to service provider after service completion
    here --user-- is feedback given user
    '''
    service             = models.ForeignKey(Service, on_delete=models.CASCADE)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    content             = models.TextField()
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.service) +' - '+str(self.user)

BOOKINGLOCATION  = (('Come to my place','Requester place'),('Service provider place','Provider place'),('Remotely','Remotely'))

class RowBooking(models.Model):
    '''
    To save row booking request given by requester

    '''
    requester                   = models.ForeignKey(User , on_delete=models.CASCADE,related_name="requester")
    service                     = models.ForeignKey(Service , on_delete=models.CASCADE)
    appointment_city            = models.ForeignKey(City,blank=True,on_delete=models.DO_NOTHING)
    appointment_venue           = models.CharField(max_length=120, blank=True,null=True,choices=BOOKINGLOCATION)
    # google geo location point
    appointment_gio_location    = models.CharField(max_length=30,blank=True,null=True)
    description                 = models.TextField(blank=True,null=True)

    # check it appointment timimg is one or can be more than one
    # if one then add a field like below

    appointment_date           = models.DateField()
    appointment_time_from      = models.TimeField()
    appointment_time_to        = models.TimeField()

    # otherwise make other model like ---ServiceProviderAvailability ----
    
    created                    = models.DateTimeField(auto_now_add=True)
    # response by provider and requester     
    isacceptedbyprovider       = models.BooleanField(default=False, help_text='accepted by provider on time') 
    isacceptedbyprovider_exp   = models.BooleanField(default=False, help_text='accepted by provider after 5 min')
    accepted_time              = models.DateTimeField(null=True,blank=True)
    ispaymentadd               = models.BooleanField(default=False)
    paymentaddtime             = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return str(self.id)


class LiveBooking(models.Model):
    '''
    when requester add payment method then booking  will come in this section
    '''
    rowbooking_id               = models.ForeignKey(RowBooking ,on_delete=models.DO_NOTHING)
    # requester                   = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    # provider                    = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    

    '''
    status 
    1 = card added (live)
    2 = ReScheduled Appointments (in process)
    3 = task completed by provider not approval by requester
    4 = task completed approved by both
    
    # extra stuff 
    on cancel appoint delete model from here


    '''

    booking_status     = models.CharField(max_length=5, blank=True,null=True)



class ReScheduledAppointments(models.Model):
    rowbooking_id           = models.ForeignKey(RowBooking ,on_delete=models.DO_NOTHING)
    re_scheduled_by         = models.ForeignKey(User,on_delete=models.CASCADE)
    re_scheduled_date       = models.DateTimeField(auto_now_add=True)
    isconfirmed_by_opp      = models.BooleanField(default=False)# is confirmed by otherside
    confirmed_by_opp_date   = models.DateTimeField(blank=True,null=True)

    # which things is re-schedule 

    def __int__(self):
        return self.rowbooking_id

    class Meta:
        verbose_name_plural = "Re-Scheduled Appointments"


class notification(models.Model):
    notification_from       = models.ForeignKey(User ,on_delete=models.DO_NOTHING,related_name='notification_from')
    notification_to         = models.ForeignKey(User ,on_delete=models.DO_NOTHING,related_name='notification_to')
    isseen_by_opposite      = models.BooleanField(default=False)
    created                 = models.DateTimeField(auto_now_add=True)
    delieverd               = models.DateTimeField(blank=True,null=True)
    isseen_opposite         = models.BooleanField(default=False)
    seen_time               = models.DateTimeField(blank=True,null=True)


    def __int__(self):
        return self.rowbooking_id

    class Meta:
        verbose_name_plural = "Re-Scheduled Appointments"








class CanceledBooking(models.Model):
    '''
    cancelled booking will come here
    '''
    rowbooking_id      = models.OneToOneField(RowBooking ,on_delete=models.DO_NOTHING)
    canceled_by        = models.ForeignKey(User ,on_delete=models.DO_NOTHING)
    cancel_date        = models.DateTimeField(auto_now_add=True)


    


    def __int__(self):
        return self.rowbooking_id

    class Meta:
        verbose_name_plural = "Canceled Booking"

class PaymentMethod(models.Model):
    '''
    payment method add by requester for perticular rowbooking

    '''
    user           = models.ForeignKey(User ,on_delete=models.DO_NOTHING)
    service        = models.ForeignKey(RowBooking ,on_delete=models.DO_NOTHING)
    name_on_card   = models.CharField(max_length=40)
    card_num       = models.CharField(max_length=15)
    card_cvv       = models.CharField(max_length=5)
    card_exp       = models.CharField(max_length=10)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = "Payment Methods"



USERTYPE = (('provider','Provider'),('requester','Requester'))

class UserOtherInfo(models.Model):
    '''
    To extend basic user model (for users extra informations)
    '''
    user            = models.OneToOneField(User , on_delete=models.CASCADE)
    phone           = models.CharField('Phone Number', max_length=15,null=True,blank=True)
    idcard          = models.CharField('ID Card Number', max_length=50,null=True,blank=True)
    isphvarified    = models.BooleanField('Is Phone Varified',default=False)
    usertype        = models.CharField(max_length=20,blank=True,null=True, choices = USERTYPE)

   
    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name = "User Other Info"
        verbose_name_plural = "User Other Infos"