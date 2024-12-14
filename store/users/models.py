from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def send_verification_email(self):
        link = reverse(
            'users:email_verification',
            kwargs={
                'email': self.user.email, 
                'code': self.code
            }
        )
        verification_link = settings.DOMAIN_NAME + link
        subject = f'Подверждение учетной записи для {self.user.username}'
        message = 'Для подверждения учетной записи для {} перейдите по ссылке: {}'.format(
            self.user.email,
            verification_link
        )

        send_mail(
            subject=subject,
            message=message,
            from_email='from@mail.ru',
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'
