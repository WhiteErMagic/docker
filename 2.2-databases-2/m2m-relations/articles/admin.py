from django.contrib import admin

from .models import Article, Scopeship, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        q_is_main_true = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            for k, v in form.cleaned_data.items():
                if k == 'is_main' and v:
                    q_is_main_true += 1

                if q_is_main_true > 1:
                    raise ValidationError('Главной темой может быть только одна')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scopeship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
