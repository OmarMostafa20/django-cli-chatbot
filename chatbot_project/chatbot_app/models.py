from django.db import models
import uuid


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.customer.name} at {self.timestamp}"


class Complaint(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    summary = models.TextField()
    complaint_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Complaint {self.complaint_id} from {self.customer.name}"
