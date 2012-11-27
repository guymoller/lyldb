# Create your views here.
from django.http import HttpResponse
from django.template.context import Context
from django.template import loader
from models import SalesFlatOrder
import cgi
import datetime
import time
import sys

def index(request):
    msg = "yep"
    t = loader.get_template('db/index.html')
    
    param_date = 'today'
    params = cgi.FieldStorage()
    if "date" in params:
        param_date = params['date'].value
    today=datetime.date.today()
    yesterday = datetime.date.today() + datetime.timedelta(days=-1)
    date = today
    if param_date == 'yesterday':
        date = yesterday
    elif param_date == 'today':
        date = today
    else:
        try:
            date = datetime.datetime(*time.strptime(param_date, "%d-%m-%Y")[:6])
        except:
            msg =  "error, could not parse '" +  param_date +  "'" + str(sys.exc_info()[0])
            date = today
    
    orders = SalesFlatOrder.objects.filter(created_at=date)
    prev_day = date + datetime.timedelta(days=-1)
    next_day = date + datetime.timedelta(days=1)
    pagination_links = {"prev": prev_day.strftime("%d-%m-%Y"),  "next": next_day.strftime("%d-%m-%Y"),}
    c = Context({
        'orders': orders,         
        'pagination_links': pagination_links,
        'msg': msg,
    })
    
    
    
    return HttpResponse(t.render(c))
    
