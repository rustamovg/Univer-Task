# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Question
from .telegram_utils import send_telegram_message


@receiver(post_save, sender=User)
def send_user_to_telegram(sender, instance, created, **kwargs):
    if created:
        message = f"👤 New User Registered!\n\nName: {instance.name}\nEmail: {instance.email}\nPhone: {instance.phone_number} "
        send_telegram_message(message)


@receiver(post_save, sender=Question)
def send_question_to_telegram(sender, instance, created, **kwargs):
    if created:
        message = f"✍️ New Question Received!\n\nName: {instance.name}\nEmail: {instance.email}\nQuestion: {instance.message}"
        send_telegram_message(message)
