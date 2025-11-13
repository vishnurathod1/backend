from django.db import models

class User(models.Model):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('trainer', 'Trainer'),
        ('trainee', 'Trainee'),
    ]
    SUBJECTS = [
        ('js', 'JavaScript'),
        ('css', 'CSS'),
        ('java', 'Java'),
        ('python', 'Python'),
        ('other', 'Other'),
    ]

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Note: In production, use hashed passwords
    userType = models.CharField(max_length=10, choices=USER_TYPES)
    subject = models.CharField(max_length=10, choices=SUBJECTS, blank=True, null=True)

    def __str__(self):
        return f"{self.email} ({self.userType})"
