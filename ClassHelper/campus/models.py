# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=12)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    term = models.CharField(max_length=45, blank=True, null=True)
    division = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentGrade(models.Model):
    student_id = models.CharField(max_length=12)
    subject_id = models.CharField(max_length=100)
    term = models.CharField(max_length=10)
    grade = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_grade'


class Subject(models.Model):
    SUBJECT_TYPE = (
        (1, '전공'),
        (0, '교양'),
    )
    subject_id = models.CharField(max_length=100, primary_key=True)
    term = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    division = models.CharField(max_length=100, blank=True, null=True)
    is_major = models.IntegerField(choices=SUBJECT_TYPE)
    class_hours = models.IntegerField()
    professor_name = models.CharField(max_length=100, blank=True, null=True)
    day1 = models.CharField(max_length=10, blank=True, null=True)
    time1 = models.CharField(max_length=10, blank=True, null=True)
    day2 = models.CharField(max_length=10, blank=True, null=True)
    time2 = models.CharField(max_length=10, blank=True, null=True)
    day3 = models.CharField(max_length=10, blank=True, null=True)
    time3 = models.CharField(max_length=10, blank=True, null=True)
    people = models.IntegerField(blank=True, null=True)
    prerequisite = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'
        unique_together = (('subject_id', 'term'),)

    def __str__(self):
        return self.subject_id

class SubjectEval(models.Model):
    idx = models.AutoField(db_column='idx', primary_key=True)
    subject = models.ForeignKey(Subject, models.DO_NOTHING, related_name='subejcteval')
    term = models.CharField(max_length=10)
    eval_content = models.CharField(max_length=1000)
    eval_grade = models.DecimalField(max_digits=5, decimal_places=2)


    class Meta:
        managed = False
        db_table = 'subject_eval'


class SubjectPrerequisite(models.Model):
    subject_name = models.CharField(max_length=100)
    prerequisite = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'subject_prerequisite'


class n_subject(models.Model):
    subject_id = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_id


class Announce(models.Model):
    announce_id = models.AutoField(db_column='announce_id',primary_key=True)
    subject_id = models.CharField(max_length=100)
    term = models.CharField(max_length=25)
    announce_title = models.CharField(max_length=100)
    announce_content = models.CharField(max_length=3000)
    announce_comment = models.CharField(max_length=3000, null=True, blank=True)
    announce_writer = models.CharField(max_length=25)
    announce_date = models.DateField(auto_now=True)

    def  __str__(self):
        return self.announce_title