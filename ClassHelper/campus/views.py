from django.shortcuts import render, redirect
import pymysql as pm
from .forms import apply_form
from django.http import HttpResponse

# Create your views here.
def index(request):
    cur_user = request.user

    if cur_user.is_authenticated:
        return render(request, "campus/index.html")
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
            print(sql, subject_id)
            curs.execute(sql, (subject_id))
            conn.commit()
            conn.close()
    return render(request, 'campus/subject_apply.html')
