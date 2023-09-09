from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10)
    age = models.CharField(max_length=25, null=True)
    image = models.ImageField(upload_to="user_profiles/",  null=True, blank=True)

    

    def __str__(self):
        return self.name
    
class Construction_Site(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="site_profiles/",  null=True, blank=True)
    num_workers = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    WORKING_STATUS = (
        ('Working', 'Working'),
        ('Halted', 'Halted'),
        ('Completed', 'Completed'),
    )
    working_status = models.CharField(max_length=50, choices=WORKING_STATUS)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Site_User(models.Model):
    name = models.OneToOneField(users, on_delete=models.CASCADE)
    TYPE_ROLE = (
        ('Sitehead', 'Sitehead'),
        ('Superviser', 'Superviser'),
        ('Technician', 'Technician'),
    )
    site_role = models.CharField(max_length=50, choices=TYPE_ROLE)
    site_data = models.ForeignKey(Construction_Site, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)


