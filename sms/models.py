from django.db import models

class Leader(models.Model):
    name = models.CharField(max_length=100)
    cluster = models.CharField(max_length=59)
    # The max_length can be 13 for numbers like +254...
    phone_number = models.CharField(max_length=13)

    def save(self, *args, **kwargs):
        # Check if the number starts with '0' and is 10 digits long
        if self.phone_number.startswith('0') and len(self.phone_number) == 10:
            # Replace the leading '0' with '+254'
            self.phone_number = '+254' + self.phone_number[1:]
        
        # Call the parent class's save method to save the object
        super(Leader, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.cluster})"


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_to = models.ManyToManyField(Leader, related_name="messages")

    def __str__(self):
        return f"Message {self.id} - {self.created_at}"
