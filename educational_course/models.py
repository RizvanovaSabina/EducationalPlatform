from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=30)
    surname = models.CharField(verbose_name="Фамилия", max_length=30)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255, unique=True)
    description = models.TextField(verbose_name="Описание", blank=False)
    duration = models.PositiveIntegerField(verbose_name="Продолжительность курса в месяцах")
    price = models.PositiveIntegerField(verbose_name="Стоимость")
    author = models.ForeignKey(
        'Autor',
        verbose_name="Автор курса",
        blank=True,
        null=True,
        related_name='courses',
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-title']

    def __str__(self):
        return self.title


class Autor(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    photo = models.ImageField(verbose_name="Фото", upload_to='photos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField('Название', max_length=100, choices=(
        ('Программирование', 'Программирование'),
        ('Менеджмент', 'Менеджмент')
    ))
    discription = models.TextField("Описание", blank=False)
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        related_name='directions',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Purchase(models.Model):
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        'Customer',
        verbose_name='Покупатель',
        related_name='purchases',
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['date_of_purchase']

    def __str__(self):
        return f'Курс для {self.customer} приобретен'


class Profile(models.Model):
    email = models.EmailField(verbose_name="Email", unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=255)
    photo = models.ImageField(verbose_name="Фото", upload_to='photos/', null=True, blank=True)
    customer = models.ForeignKey(
        'Customer',
        verbose_name='Ученик',
        related_name='profiles',
        blank=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['email']

    def __str__(self):
        return self.email






