from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):  # Usa TabularInline para mostrar las opciones en un formato compacto
    model = Choice
    extra = 3  # Permite agregar hasta 3 opciones por defecto


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)

# Register your models here.
