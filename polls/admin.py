from django.contrib import admin
from .models import  *
# Register your models here.
class ChoiceInline(admin.TabularInline):
 model= Choice
 extra = 3

class QuestionAdmin(admin.ModelAdmin):
 fieldsets=[
     ("Poll question", {'fields': ['question']}),
    ('Date information', {'fields': ['vote_date'], 'classes': ['collapse']}),
            ]
 inlines = [ChoiceInline]
 list_display = ('question', 'vote_date')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text','votes']

admin.site.register(Choice,ChoiceAdmin)
# admin.site.register(Poll)
admin.site.register(Poll, QuestionAdmin)