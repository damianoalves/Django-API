from django.contrib import admin
from guardian.admin import GuardedModelAdmin


class BaseAdmin(admin.ModelAdmin):
    exclude = ('updated_by', 'created_by', 'deleted_by', 'deleted_at')

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        elif not change:
            obj.updated_by = request.user
            obj.created_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if not change:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.created_by = request.user
                instance.updated_by = request.user
                instance.save()
        elif change:
            instances = formset.save(commit=False)
            for instance in instances:
                if hasattr(instance, 'created_by') and not instance.created_by:
                    instance.created_by = request.user
                instance.updated_by = request.user
                instance.save()


class GuardedBaseAdmin(GuardedModelAdmin, BaseAdmin):
    list_filter = ('user', )
