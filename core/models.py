from django.contrib.auth.models import User
from django.db import models
from model_utils.fields import UUIDField
from model_utils.managers import SoftDeletableManager
from model_utils.models import SoftDeletableModel, UUIDModel


class BaseModel(SoftDeletableModel):

    uuid = UUIDField(
        primary_key=False,
        version=4,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Deleted at"
    )

    created_by = models.ForeignKey(
        User,
        null=True,
        verbose_name="Created by",
        related_name='%(class)s_created_by',
        on_delete=models.CASCADE
    )

    updated_by = models.ForeignKey(
        User,
        null=True,
        verbose_name="Updated by",
        related_name='%(class)s_updated_by',
        on_delete=models.CASCADE
    )

    deleted_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name="Deleted by",
        related_name='%(class)s_deleted_by',
        on_delete=models.CASCADE
    )

    objects = SoftDeletableManager()

    def __str__(self):
        if hasattr(self, 'name'):
            return "%s" % self.name
        if hasattr(self, 'description'):
            return "%s" % self.description
        if self._meta.verbose_name:
            return "%s" % self._meta.verbose_name

        return self.pk

    def __unicode__(self):
        if hasattr(self, 'name'):
            return u"%s" % self.name
        if hasattr(self, 'description'):
            return u"%s" % self.description
        if self._meta.verbose_name:
            return u"%s" % self._meta.verbose_name

        return self.pk

    @classmethod
    def list(cls, *args, **kwargs):
        return cls.objects.filter(*args, **kwargs)

    @classmethod
    def count(cls, *args, **kwargs):
        return cls.list(*args, **kwargs).count()

    @classmethod
    def create(cls, **kwargs):
        cls.objects.create(**kwargs)

    @classmethod
    def get(cls, *args, **kwargs):
        return cls.list(*args, **kwargs).first()

    @classmethod
    def choices(cls):
        choices = ()

        for model in cls.objects.all():
            choice = (model.pk, model.name if hasattr(model, 'name') else model.pk)
            choices += choice

        return choices

    @classmethod
    def retrieve(cls, **kwargs):
        return cls.list(**kwargs).first()

    class Meta:
        abstract = True
