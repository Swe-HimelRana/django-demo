from django.shortcuts import render
import datetime
from .helpers import isMobile

# Create your views here.

# Index page
def index(request):
    today = datetime.date.today().strftime("%A")
    currentMonthNmae = datetime.date.today().strftime("%B")

    week   = ['Sunday', 
              'Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday']
    year = [
        'January',
        'February', 
        'March', 
        'April', 
        'May', 
        'June', 
        'July', 
        'August', 
        'September', 
        'October', 
        'November', 
        'December'
    ]
    countries = [
        "Albania",
        "Algeria",
        "Andorra",
        "Angola",
        "Australia"
    ]
    

    context = {
        'today': today,
        'thismonth': currentMonthNmae,
        'fullweek': week,
        'fullyear': year,
        'countries': countries
    }

    # Detecting mobile/dekstop browser and returning views
    user_agent = request.META['HTTP_USER_AGENT']

    if isMobile(user_agent):
        return render(request,'apps/dashboard/index-mobile.html', context=context)
    else:
      return render(request,'apps/dashboard/index.html', context=context)

# Char Page
def chart(request):
    return render(request,'apps/dashboard/chart.html',)

# Contries Page
def countries(request):
    countries = [
        "Albania",
        "Algeria",
        "Andorra",
        "Angola",
        "Australia",
    ]

    context = {
        'countries': countries
    }

    return render(request,'apps/dashboard/countries.html', context=context)