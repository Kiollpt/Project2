from django.contrib import admin

# Register your models here.
from .models import Question, Choice,Comment


class ChoiceInline(admin.TabularInline):
    model =Choice
    extra=2
class QuestionAdmin(admin.ModelAdmin):
    inlines =[ChoiceInline]
    list_display =('question_text','pub_date','was_published_recently')


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)


#2017.9.19 Add posting board#
admin.site.register(Comment)
#2017.9.19 Add posting board#
