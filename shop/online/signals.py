from django.db.models.signals import post_save, pre_save, post_delete, pre_delete, pre_init, post_init
from django.dispatch import receiver
from .models import Review, Notification, Product, User
from django.db.models import Avg
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Review)
def create_notidication_for_partner(sender, instance: Review, created: bool, **kwargs):
    """
    Сигнал post_save вызывается после сохраниения или обновления 
    Параметр created - означает создан ли instance или изменен
    True - создан / False - объект был измен
    """
    if created:
        product = instance.product
        owner = product.owner

        average_raiting = product.reviews.aggregate(Avg('rating')).get('rating__avg', None)

        if average_raiting is not None and average_raiting <= 4.5:
            notification_text = f'Attention: The average rating of your product {product.name} has fallen below 4.5.'
            Notification.objects.create(
                recipient=owner,
                text=notification_text,
                level=Notification.ATTENTION
            )

        review_notification_text = f'New review for your product {product.name} by {instance.user.username}'
        Notification.objects.create(
            recipient=owner,
            text=review_notification_text,
            level=Notification.INFORMATIVE
        )


@receiver(pre_save, sender=Product)
def validate_product_description(sender, instance: Product, **kwargs):
    """
    Сигнал pre_save вызывается перед сохранением объекта
    created отсутствует!
    """
    # добавляем ко всем описаниям(поле description) обязательные слова
    instance.description = instance.description + ' Ляляля Тополя =)'


@receiver(post_delete, sender=Product)
def delete_product_post(sender, instance: Product, using, **kwargs):
    """
    Сигнал post_delete вызывается после удаления объекта
    Параметр created отсутствует!
    using - параметр содержащий имя Базы Данных
    """
    logging.info(f'База данных {using}')
    Notification.objects.create(
            recipient=instance.owner,
            text=f'Продукт {instance.name} был удален из карточек товаров',
            level=Notification.INFORMATIVE
        )
    

@receiver(pre_delete, sender=Product)
def delete_product_pre(sender, instance: Product, using, **kwargs):
    """
    Сигнал pre_delete вызывается до удаления объекта
    Параметр created отсутствует!
    using - параметр содержащий имя Базы Данных
    """
    logger.info(f'База данных {using}')
    # какие-бы то ни было действия до удаления объекта
    Notification.objects.create(
            recipient=instance.owner,
            text=f'Продукт {instance.name} БУДЕТ удален из карточек товаров',
            level=Notification.INFORMATIVE
        )
    

@receiver(pre_init, sender=User)
def create_user_pre_init(sender, args, kwargs, **extras):
    """
    Сигнал pre_init вызывается до того, как будет выполнена инициализация объекта.
    args: Позиционные аргументы, передаваемые при создании объекта.
    kwargs: Именованные аргументы, передаваемые при инициализации объекта.
    extras: Дополнительные аргументы
    instance НЕТ.
    """
    logger.info(f"Initializing Product with args: {args}, kwargs: {kwargs}")
    

@receiver(post_init, sender=User)
def create_user_post_init(sender, instance: User, **kwargs):
    """
    Сигнал post_init вызывается после того, как будет выполнена инициализация объекта.
    Отправляется всякий раз, когда экземпляр модели создается или загружается из базы данных
    instance: экземпляр
    """
    logger.info(instance.username)