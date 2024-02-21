from django.db import models

# Create your models here.


class StudentData(models.Model):
    GENDER_CHOICES=(
        ("male", "Male"),
        ("female", "Female")
    )
    name=models.CharField(max_length=120)
    email=models.EmailField(max_length=200)
    birth_date=models.DateField()
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=8, choices=GENDER_CHOICES)

    def __str__(self) -> str:
        return self.name
    
















# class Email(models.Model):
#     email = models.EmailField(max_length=200)

#     def __str__(self) -> str:
#         return self.email
    
# class Date(models.Model):
#     date = models.DateField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.date
    
# class A