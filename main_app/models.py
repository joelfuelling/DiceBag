from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator


#* I FULLY realize a dice roll should go up to 100... However, for the homework I'm limiting it to 20.

RESULTS = ( # Constant variable are CAPS as convention in Django. #! WILL NOT CHANGE.
    ('1', 'Nat 1 :('),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', 'Nat 20!'),
)
# Create your models here.
class Die(models.Model):
    sides = models.IntegerField()
    material = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)

    def __str__(self):
        return self.text_color
    
    # Add this method
    def get_absolute_url(self):
        return reverse("die_detail", kwargs={"pk": self.id})
    
class Rolls(models.Model):
    date = models.DateField('Rolled on') # Unfortunately, the Rolls Date field is just a basic text input. This is what Django uses by default for DateFields.
    result = models.PositiveIntegerField(
        validators=[MaxValueValidator(20)],
        choices=RESULTS,
        default=RESULTS[0][0] # Tuples use [] syntax Default is '1', '1'
    )
    die = models.ForeignKey(Die, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_result_display()} on {self.date}' #? get_result_display() = Magic django method. pulls out the human readable '1', '2', etc., from the choice value

    