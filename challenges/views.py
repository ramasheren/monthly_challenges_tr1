from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk 5 kilometers every day!",
    "march": "Learn Django for at least 30 minutes every day!",
    "april": "Practice coding for at least 1 hour every day!",
    "may": "Read one book every week!",
    "june": "Meditate for 10 minutes every day!",
    "july": "Drink 2 liters of water every day!",
    "august": "Write a journal entry every day!",
    "september": "Run 3 kilometers every day!",
    "october": "Learn a new language for at least 30 minutes every day!",
    "november": "Volunteer for a local charity once a week!",
    "december": None,
}

def index (reuest):
    months = list(monthly_challenges.keys())
    list_items = ""
    for month in months:
        list_items += f"<li><a href='{reverse('monthly-challenge', args=[month])}'>{month.title()}</a></li>"
    return HttpResponse(f"<h1>Monthly Challenges</h1><ul>{list_items}</ul>")

def monthly_challenge(request, month):
    try:
        month = month.lower()
        challenge = monthly_challenges[month]
        return HttpResponse(challenge)
    except KeyError:
        return HttpResponseNotFound("This month is not valid.")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
