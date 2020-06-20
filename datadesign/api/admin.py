from django.contrib import admin

# Register your models here.

from api.models import Agent, Event, Group, GroupUser, User


class AgentModel(admin.ModelAdmin):
    list_display = ("id", "name", "status", "env", "version", "address")


class EventModel(admin.ModelAdmin):
    list_display = ("id", "level", "data", "arquivado", "date", "agent_id", "user_id")


class GroupModel(admin.ModelAdmin):
    list_display = ("id", "name")


class GroupUserModel(admin.ModelAdmin):
    list_display = ("id", "group_id", "user_id")


class UserModel(admin.ModelAdmin):
    list_display = ("id", "name", "last_login", "email", "password")


admin.site.register(Agent, AgentModel)
admin.site.register(Event, EventModel)
admin.site.register(Group, GroupModel)
admin.site.register(GroupUser, GroupUserModel)
admin.site.register(User, UserModel)
