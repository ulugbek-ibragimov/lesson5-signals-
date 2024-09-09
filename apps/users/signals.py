from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete
from apps.users.models import User, UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        user_profile = UserProfile.objects.get(pk=instance.pk)
        user_profile.user = instance

@receiver(post_delete, sender=UserProfile)
def delete_user_profile(sender, instance, **kwargs):
    user = User.objects.get(pk=instance.pk)
    user.delete()
    print("user successfully deleted!")

#------------------------------------------------------
# @receiver(post_delete, sender=UserProfile)
# def delete_user(sender, instance, **kwargs):
#     user = User.objects.get(pk=instance.pk)
#     user.delete()
#     print("user successfully deleted!")


