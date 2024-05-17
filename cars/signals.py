from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car
from cars.models import CarInventory


#sk-proj-qEjMrTmXWQbrhjG0xKgBT3BlbkFJTTqqjj5ao9X4jM0IVx6X chave openai


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    ) ['total_value']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )


"""""""""
@receiver(pre_save, sender = Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_aibio(instance.model, instance.brand, instance.model_year)
        instance.bio = ai_bio

"""""



@receiver(post_save, sender = Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender = Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
