from django.db import models
# Create your models here.


class users(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	phone=models.CharField(max_length=100);
	stz=models.CharField(max_length=20);

class users_locations(models.Model):
	email=models.CharField(max_length=100);
	addr_type=models.CharField(max_length=100);
	address=models.CharField(max_length=500);
	zip=models.CharField(max_length=50);
	city=models.CharField(max_length=100);

class prod_category(models.Model):
	cat_name=models.CharField(max_length=100);
	
class products(models.Model):
	cat_id=models.CharField(max_length=10);
	cat_name=models.CharField(max_length=100);
	prod_name=models.CharField(max_length=100);
	cost=models.FloatField(max_length=100);
	photo = models.CharField(max_length=500);
	availability=models.IntegerField();
	description=models.TextField();
	sid=models.CharField(max_length=500);
	sales=models.IntegerField();



class seller(models.Model):
	sid=models.CharField(max_length=100);
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	phone=models.CharField(max_length=100);
	address=models.CharField(max_length=200);
	stz=models.CharField(max_length=20)


class cart(models.Model):
	email=models.CharField(max_length=100);
	pid=models.CharField(max_length=10);
	prod_name=models.CharField(max_length=100);
	unit_cost=models.FloatField(max_length=100);
	tot_cost=models.FloatField(max_length=100);
	quantity=models.IntegerField();
	photo = models.CharField(max_length=500);
	d_date=models.CharField(max_length=100);
	sid=models.CharField(max_length=100);

class orders(models.Model):
	oid=models.IntegerField();
	email=models.CharField(max_length=100);
	pid=models.CharField(max_length=10);
	prod_name=models.CharField(max_length=100);
	unit_cost=models.FloatField(max_length=100);
	tot_cost=models.FloatField(max_length=100);
	photo = models.CharField(max_length=500);
	quantity=models.IntegerField();
	d_date=models.CharField(max_length=100);
	stz=models.CharField(max_length=100);
	progress=models.IntegerField();
	sid=models.CharField(max_length=100);


class coupons(models.Model):
	code=models.CharField(max_length=159);
	discount=models.IntegerField();
	stz=models.CharField(max_length=159);
