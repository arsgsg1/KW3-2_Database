from django.shortcuts import render, redirect
from .forms import apply_form
from .models import Announce, Subject, SubjectEval
from django.db import connection

# Create your views here.
def index(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        student_id = request.user.username
        sql = "select sub.subject_id, subject_name, professor_name, class_hours, day1, time1, day2, time2, day3, time3 from subject as sub join student_grade as gra on sub.subject_id=gra.subject_id where gra.student_id={} and gra.term='2020-2' and sub.term='2020-2'".format(student_id)
        subjects = Subject.objects.raw(sql)

        announce_list = {}
        for subject in subjects:
            subject_id = subject.subject_id
            announce_list = {
                subject_id: Announce.objects.filter(subject_id=subject_id).values()
            }

        data = {
            'subject_list': subjects,
            'announce_list' : announce_list,
            'friend_list' : get_friend_list(),
            'friend_subject_list' : get_friend_subject_list()
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
            sql = "insert into student_grade(student_id, subject_id, term) select 2015722083, subject_id, term from subject where subject_id={} and term='2020-2';".format(subject_id)
            Subject.objects.raw(sql)

    return render(request, 'campus/subject_apply.html')


def get_friend_list(self=0):
    with connection.cursor() as cursor:
        sql = """select student.name from student where student_id in (
            select distinct gra.student_id
            from (subject as sub join student_grade as gra on sub.subject_id=gra.subject_id) where gra.term='2020-2' and sub.term='2020-2' and gra.student_id in (select A.friend_id from friend as A join friend as B where A.student_id=B.friend_id and B.student_id=A.friend_id and A.student_id='2015722052'));
            """
        cursor.execute(sql)
        row = cursor.fetchone()
    return row


def get_friend_subject_list(self=0):
    with connection.cursor() as cursor:
        sql = """select sub.subject_id, subject_name, professor_name, class_hours, day1, time1, day2, time2, day3, time3
            from (subject as sub join student_grade as gra on sub.subject_id=gra.subject_id) where gra.term='2020-2' and sub.term='2020-2' and gra.student_id in (select A.friend_id from friend as A join friend as B where A.student_id=B.friend_id and B.student_id=A.friend_id and A.student_id='2015722052');
            """
        cursor.execute(sql)
        row = cursor.fetchone()
    result = ''
    for item in row:
        result = result + str(item) + ' '
    return result

def get_avg_score(self=0):
    with connection.cursor() as cursor:
        sql = """with
            eval_avg(average) as (select avg(eval_grade) from subject_eval),
            eval_std(derivation) as (select stddev(eval_grade) from subject_eval)
            select avg(truncate(((eval_grade-average)/ derivation),2)) as z_score from subject_eval , eval_avg, eval_std
             where subject_id='H020-1-8297-02' and term='2020-2' group by subject_id, term;
            """
        cursor.execute(sql)
        row = cursor.fetchone()
    return row

def subject_eval(request, subject_id):
    #강의 평가
    evals = SubjectEval.objects.filter(subject_id=subject_id).values()
    subject_name = Subject.objects.filter(subject_id=subject_id).first().subject_name
    z_score = get_avg_score()[0]
    context = {
        'evals' : evals,
        'subject_name' : subject_name,
        'z_score' : z_score
    }
    return render(request, 'campus/subject_eval.html', context)


def grade(request):
    return render(request, 'campus/grade.html')

def test1(request):
    return render(request, 'campus/index.html')