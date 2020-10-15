from django.shortcuts import render, redirect
from .forms import EmailForm
from .validation import check_recipients, send_email
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "emailapp/index.html")


def email_form_view(request):
    email_form = EmailForm()
    if request.method == 'POST':
        email_form = EmailForm(request.POST)

        if email_form.is_valid():
            print("Validation Success!")

            email = str(email_form.cleaned_data['email_address'])
            password = str(email_form.cleaned_data['password'])
            subject = str(email_form.cleaned_data['subject'])
            text = str(email_form.cleaned_data['text'])

            print("Checking recipients...")
            recipients = check_recipients(str(email_form.cleaned_data['receivers']))

            print("Sending the email...")
            send_email(email, password, recipients, subject, text)

            messages.success(request, "Message Sent!")

            print("Messages Sent!")
            print("Sent to: ")
            for address in recipients:
                print(address)

            return redirect("emailapp:home")

        else:
            email_form = EmailForm()
            messages.error(request, "Failed to send email.")

    return render(request, "emailapp/email_form.html", {"form": email_form})