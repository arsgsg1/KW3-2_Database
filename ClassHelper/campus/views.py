from django.shortcuts import render, redirect
import pymysql as pm
from .forms import apply_form
from .models import Announce, Subject
from django.http import HttpResponse

# Create your views here.
def index(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        student_id = request.user.username
        # select
        #conn = pm.connect(host='localhost', user='django_admin', password='s852130', db='registration', charset='utf8')
        #curs = conn.cursor()
        sql = "select sub.subject_id, subject_name, professor_name, class_hours, day1, time1, day2, time2, day3, time3 from subject as sub join student_grade as gra on sub.subject_id=gra.subject_id where gra.student_id={} and gra.term='2020-2' and sub.term='2020-2'".format(student_id)
        subjects = Subject.objects.raw(sql)

        #sql = "select sub.subject_id, subject_name, professor_name, class_hours, day1, time1, day2, time2, day3, time3 from subject as sub join student_grade as gra on sub.subject_id=gra.subject_id where gra.student_id=%s and gra.term='2020-2' and sub.term='2020-2'"
        #curs.execute(sql, (student_id))
        #subjects = curs.fetchall()
        #conn.close()

        announce_list = {}
        for subject in subjects:
            subject_id = subject.subject_id
            announce_list = {
                subject_id: Announce.objects.filter(subject_id=subject_id).values()
            }

        data = {
            'subject_list': subjects,
            'announce_list' : announce_list
        }
        return render(request, "campus/main.html", data)
    else:
        return redirect('/common/login')


def subject_apply(request):
    if request.method == "POST":
        #insert
        form = apply_form(request.POST)
        if form.is_valid():
            subject_id = form.cleaned_data['subject_id']
            conn = pm.connect(host='localhost', user='django_admin', password='s852130', db='registration', charset='utf8')
            curs = conn.cursor()
            sql = "insert into student_grade(student_id, subject_id, term) select 2015722083, subject_id, term from subject where subject_id=%s and term='2020-2';"
            curs.execute(sql, (subject_id))
            conn.commit()
            conn.close()
    return render(request, 'campus/subject_apply.html')


def test1(request):
    return render(request, 'campus/index.html')