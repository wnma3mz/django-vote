from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionPostAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionPostAdmin)
