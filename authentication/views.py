import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.html import strip_tags, escape
from django.utils.crypto import get_random_string
from .models import User


class SignUpView(View):
    template_name = 'auth/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = escape(strip_tags(request.POST.get('fname', '')))
        last_name = escape(strip_tags(request.POST.get('lname', '')))
        email = escape(strip_tags(request.POST.get('email', ''))).lower()
        username = escape(strip_tags(request.POST.get('username', '')))
        role = escape(strip_tags(request.POST.get('role', '')))
        password = get_random_string(length=8)
        # Check if email is available
        email_taken = User.objects.get(email=email)
        if email_taken:
            # Email taken
            data = {'status': 400, 'msg': 'Unable To Create Account.'}
        else:
            # Email availabel and Create User
            user = User.objects.create_user(username=username, email=email, role=role,
                                            first_name=first_name, last_name=last_name,
                                            password=password)
            if user:
                data = {'status': 201,
                        'msg': user.firstname+'`s Account Created Successfuly.'}
            else:
                data = {'status': 500, 'msg': 'Unable To Create Account.'}
        return HttpResponse(json.dumps(data))
