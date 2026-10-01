from django.db import models

class tbl_district(models.Model):
    district_name = models.CharField(max_length=100)

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)

class tbl_place(models.Model):
    place_name = models.CharField(max_length=100)
    district = models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_user(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_address = models.CharField(max_length=100)
    place = models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_password = models.CharField(max_length=100)
    user_status = models.IntegerField(default=0)
    user_photo = models.FileField(upload_to="Assets/UserDocs")