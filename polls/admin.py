from django.contrib import admin
from django.contrib.admin.sites import site

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # por defecto agrega 3 choices en admin

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)