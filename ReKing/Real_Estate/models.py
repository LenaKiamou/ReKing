from django.db import models


TYPE_CHOICES = [
    ('appartment', 'Διαμέρισμα'),
    ('building', 'Κτήριο'),
    ('plot', 'Οικόπεδο'),
    ('detached', 'Μονοκατοικία'),
    ('maisonette', 'Μεζονέτα'),  
]

FLOOR_CHOICES = [
    ('underground', 'Υπόγειο'),
    ('semiground', 'Ημιυπόγειο'),
    ('ground', 'Ισόγειο'),
    ('semifloor', 'Ημιώροφος'),
    ('first', '1oς'),
    ('second', '2oς'),
    ('third', '3oς'),
    ('forth', '4oς'),
    ('fifth', '5oς'),
    ('sixth', '6oς'),
    ('seventh', '7oς'),
    ('plus', '8oς+'),
]


class Features(models.Model):
    feature = models.CharField("Πρόσθετες παροχές", max_length=48)

    def __str__(self):
        return f"{self.feature}"


class House(models.Model):
    type = models.CharField("Είδος", choices=TYPE_CHOICES, max_length=24)
    floor = models.CharField("Όροφος", choices=FLOOR_CHOICES, max_length=24)
    area = models.IntegerField("Εμβαδόν (τ.μ)")
    rooms = models.IntegerField("Δωμάτια")
    year_constructed = models.IntegerField("Έτος κατασκευής", null=True, blank=True)
    year_revovated = models.IntegerField("Έτος ανακαίνισης", null=True, blank=True)
    price = models.PositiveIntegerField("Τιμή")
    city = models.CharField("Πόλη", max_length=24)
    district = models.CharField("Περιοχή", max_length=24)
    address = models.CharField("Οδός", max_length=24)
    number = models.IntegerField("Αριθμός")
    zipcode = models.IntegerField("T.K")
    description = models.TextField("Περιγραφή", max_length=5000, null=True, blank=True)
    image = models.ImageField(upload_to='Real_Estate/static/images/')
    google_url = models.URLField("google_url", null=True, blank=True)
    more_features = models.ManyToManyField(Features, blank=True, verbose_name="Πρόσθετες παροχές")


class Images(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='Real_Estate/static/images/')