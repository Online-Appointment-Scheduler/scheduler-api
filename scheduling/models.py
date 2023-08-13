# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AttendEventRequest(models.Model):
    event = models.ForeignKey('Event', models.CASCADE)
    member = models.ForeignKey('Member', models.CASCADE)
    is_pending = models.BooleanField()
    description = models.CharField(max_length=150, blank=True, null=True)
    is_cancelled = models.BooleanField()

    class Meta:
        unique_together = (('event', 'member'),)


class Blacklist(models.Model):
    manager = models.ForeignKey('Manager', models.CASCADE)
    member = models.ForeignKey('Member', models.CASCADE)


class Event(models.Model):
    title = models.CharField(max_length=50)
    event_description = models.CharField(max_length=500, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_recurring = models.BooleanField()
    created_by = models.ForeignKey('authentication.CustomUser', models.CASCADE, db_column='created_by')
    created_date = models.DateField()
    parent_event = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)


class EventInstanceException(models.Model):
    event = models.ForeignKey(Event, models.CASCADE)
    is_rescheduled = models.BooleanField()
    is_cancelled = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey('authentication.CustomUser', models.CASCADE, db_column='created_by')
    created_date = models.DateField()


class Lobby(models.Model):
    manager = models.ForeignKey('Member', models.CASCADE, db_column='manager')


class LobbyJoinRequest(models.Model):
    lobby = models.ForeignKey(Lobby, models.CASCADE)
    member = models.ForeignKey('Member', models.CASCADE)

    class Meta:
        
        unique_together = (('lobby', 'member'),)


class Manager(models.Model):
    user = models.OneToOneField('authentication.CustomUser', models.DO_NOTHING, primary_key=True)


class Member(models.Model):
    user = models.OneToOneField('authentication.CustomUser', models.DO_NOTHING, primary_key=True)
    status = models.CharField(max_length=20, blank=True, null=True)


class MembersToLobby(models.Model):
    lobby = models.ForeignKey(Lobby, models.DO_NOTHING)
    member = models.ForeignKey(Member, models.DO_NOTHING)


class RecurringPattern(models.Model):
    event = models.OneToOneField(Event, models.DO_NOTHING, primary_key=True)
    recurring_type = models.ForeignKey('RecurringType', models.DO_NOTHING)
    separation_count = models.SmallIntegerField(blank=True, null=True)
    day_of_week = models.SmallIntegerField(blank=True, null=True)
    week_of_month = models.SmallIntegerField(blank=True, null=True)
    day_of_month = models.SmallIntegerField(blank=True, null=True)
    month_of_year = models.SmallIntegerField(blank=True, null=True)


class RecurringType(models.Model):
    type = models.CharField(max_length=20)
