# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

from postmarker.core import PostmarkClient


# @periodic_task(run_every=(crontab()), 
# 	name="first", 
# 	ignore_result=True)
@shared_task
def first():
	# z = x + y 
	# print(z)
	
	postmark = PostmarkClient(server_token=settings.API_TOKEN)
	print(postmark)
	email = postmark.emails.Email(
	From='chiragkanhasoft@nrmkanhasoft.xyz',
	To='sonu.kanhasoft@gmail.com',
	Subject='Postmark test',
	HtmlBody='<html><body><strong>Hello</strong> dear Postmark user.</body></html>')
	email.attach('/home/sys25/Documents/Dhruv Naik - Requirement  Document.odt')
	email.send()
	print("Hello world!")


# @periodic_task(run_every=(crontab()))
# def sending_email():
# 	recipient_list = ['sonu.kanhasoft@gmail.com']
# 	subject = 'Testing'
# 	text_content = 'This is an important message.'
# 	cc = ['gsonu472@gmail.com']
# 	html_content = render_to_string("myapp/emailtemplate.html")
# 	email_from = settings.EMAIL_HOST_USER
# 	msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list, cc)
# 	msg.attach_alternative(html_content, "text/html")
# 	msg.attach_file('/home/sys25/Documents/Dhruv Naik - Requirement  Document.odt')
# 	msg.send()

# @task()
# def first(x,y):
# 	z = x + y 
# 	print(z)
# 	print("Hello world!")
# 	return z

# # Other Celery settings
# CELERY_BEAT_SCHEDULE = {
#     'first': {
#         'task': 'myapp.tasks.first',
#         'schedule': crontab(),
#     }
# }

@shared_task
def add(x, y):
	z = x + y
	print(z)
	return z


@shared_task
def mul(x, y):
	z = x*y
	print(z)
	return z


@shared_task
def xsum(numbers):
    return sum(numbers)
