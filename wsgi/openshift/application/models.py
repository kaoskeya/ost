from django.db import models

# Create your models here.

class Payment(models.Model):
	PAYMENT_MODES = (
		('CHECK', 'Check'),
		('CASH', 'Cash'),
		('ONLINE', 'Online'),
		('DD', 'Demand Draft')
	)
	name = models.CharField(max_length=64)
	mode = models.CharField(max_length=10, choices=PAYMENT_MODES)
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	info = models.TextField()
	timestamp = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%d" % self.id

class Application(models.Model):
	GENDER_SIZES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	APP_STATUS = (
        ('PROCESSING', 'Processing'),
        ('REJECTED', 'Rejected'),
    )
	name = models.CharField(max_length=64)
	gender = models.CharField(max_length=1, choices=GENDER_SIZES)
	dob = models.DateField()
	placeofbirth = models.CharField("Place of birth", max_length=32)
	religion = models.CharField(max_length=32)
	parent_one_name = models.CharField("Parent One Name", max_length=64)
	parent_one_phone = models.CharField("Parent One Phone", max_length=32)
	parent_one_email = models.EmailField("Parent One Email")
	parent_two_name = models.CharField("Parent Two Name", max_length=64)
	parent_two_phone = models.CharField("Parent Two Phone", max_length=32, blank=True)
	parent_two_email = models.EmailField("Parent Two Email", blank=True)
	payment = models.OneToOneField(Payment)
	status = models.CharField(max_length=16, choices=APP_STATUS, default='PROCESSING')

	def __unicode__(self):
		return  " %d %s " % (self.id, self.name)