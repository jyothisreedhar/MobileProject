from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=120)
    price = models.FloatField()
    specs = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product_name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    address = models.CharField(max_length=120)
    choices = (
        ('ordered', 'ordered'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled')
    )
    status = models.CharField(max_length=120, choices=choices, default="ordered")
    user = models.CharField(max_length=120)


class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    # price=models.(Product,on_delete=models.CASCADE)
    total_price=models.PositiveIntegerField(editable=False,blank=True,null=True)
    user=models.CharField(max_length=120)

    # class Cart(models.Model):
    #     product = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    #     quantity = models.PositiveBigIntegerField(default=1)
    #     price_total = models.PositiveBigIntegerField(editable=False, blank=True, null=True)
    #     user = models.CharField(max_length=120, null=True)
    #
    #     def save(self, *args, **kwargs):
    #         self.price_total = self.product.price * self.quantity
    #         super(Cart, self).save(*args, **kwargs)

    def save(self,*args,**kwargs):
        self.total_price=self.product.price*self.quantity
        super(Cart, self).save(*args,**kwargs)

# create table product(product_name varchar(25),price float(),spcs,images)


# user:jyothi
# pswd:lakshmi123
