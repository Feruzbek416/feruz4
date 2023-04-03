from django.db import models

# Create your models here.

class Author(models.Model):
    NameType = models.TextChoices('NameType','Nike Adidas Gucci')
    name1 = models.CharField(max_length=60,blank=True,choices=NameType.choices)
    
    def __str__(self):
        return self.name1
class Blog(models.Model):
    name = models.CharField(max_length=60)
    img= models.ImageField(upload_to='image/')
    ColorType = models.TextChoices('ColorType', 'WHITE BLACK BLUE White_and_Black')
    color = models.CharField(max_length=60,blank=True,choices=ColorType.choices)
    SizeType = models.TextChoices('SizeType','38 39 40 41 42 43 44')
    size = models.CharField(max_length=60,blank=True,choices=SizeType.choices)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):  
        return self.name