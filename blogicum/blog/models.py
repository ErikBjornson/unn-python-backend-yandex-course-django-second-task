from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseModel(models.Model):
    """Базовый класс для создания повторяющихся полей (соблюдение DRY)."""

    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )

    created_at = models.DateTimeField(
        blank=False,
        auto_created=True,
        auto_now_add=True,
        verbose_name="Добавлено",
    )

    class Meta:
        abstract = True


class Category(BaseModel):
    """Модель тематической категории."""

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=256,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=False,
    )
    slug = models.SlugField(
        verbose_name="Идентификатор",
        help_text=(
            "Идентификатор страницы для URL; "
            "разрешены символы латиницы, "
            "цифры, дефис и подчёркивание."
        ),
        unique=True,
        blank=False,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"


class Location(BaseModel):
    """Модель географической метки."""

    name = models.CharField(
        verbose_name="Название места",
        max_length=256,
        blank=False,
    )

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"


class Post(BaseModel):
    """Модель публикации."""

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=256,
        blank=False,
    )
    text = models.TextField(
        verbose_name="Текст",
        blank=False,
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — "
            "можно делать отложенные публикации."
        ),
        blank=False,
    )

    author = models.ForeignKey(
        verbose_name="Автор публикации",
        to=User,
        blank=False,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        verbose_name="Местоположение",
        to=Location,
        null=True,
        on_delete=models.SET_NULL,
    )
    category = models.ForeignKey(
        verbose_name="Категория",
        to=Category,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
