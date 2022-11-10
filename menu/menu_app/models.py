from django.db import models


class Menu_Item(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    spice_level = models.SmallIntegerField(null=True)
    category = models.ForeignKey(
        "Category", 
        on_delete=models.CASCADE,
    null=True)
    cuisine = models.ForeignKey(
        "Cuisine",
        on_delete=models.CASCADE,
    null=True)
    def __str__(self):
        return self.title + ' $' + str(self.price)

    # def __str__(self):
    #     return self.title + " " + str(self.published_year) + " " + self.genre

    # ...

class Category(models.Model):
    title = models.CharField(max_length=40)
    def __str__(self):
        return self.title


class Cuisine(models.Model):
    title = models.CharField(max_length=40)
    def __str__(self):
        return self.title
    # author = models.ManyToManyField(to)

# class genres(models.Model):
