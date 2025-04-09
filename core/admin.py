from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "user", "created_at", "like_count")
    search_fields = ("content",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    raw_id_fields = ("question",)

    def like_count(self, obj):
        return obj.likes.count()

    like_count.short_description = "Likes"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
