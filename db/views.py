# Create your views here.
from django.http import HttpResponse
from django.template.context import Context
from django.template import loader
from models import SalesFlatOrder
from datetime import date, timedelta,datetime
import time
from itertools import groupby
from django.utils.datetime_safe import strftime

def index(request):
    """
    start, end expect the format yyyy-mm-dd
    """
    msg = "yep"
    t = loader.get_template('db/index.html')
    if request.GET.get('start'): 
        start_date = convert_to_date(request.GET.get('start'))
    else:
        start_date = datetime.now() + timedelta(days=-30) #30 days 
    if request.GET.get('end'):
        end_date=convert_to_date(request.GET.get('end'))
    else:
        end_date = datetime.now()
    orders = SalesFlatOrder.objects.filter(created_at__gte = start_date).filter(created_at__lte = end_date).order_by('created_at')
    orders_by_date = []
    
    for day, order_group in groupby(orders,lambda o: strftime(o.created_at, "%d-%m-%Y")):
        orders_by_date.append ({'day':day, 'display_date': day.replace('-','.')[:-5],  'orders': list(order_group)})
        
    for row in orders_by_date:
        
        row['revenues']= sum([x.grand_total for x  in row['orders']])
        row['count'] = len(row['orders'])
    
    orders_by_date_reverse = orders_by_date[:]
    orders_by_date_reverse.reverse()
    c = Context({
        'orders': orders,
        'orders_by_date':orders_by_date,  
        'orders_by_date_reverse':orders_by_date_reverse,            
        'msg': msg,
        'start_date':start_date,
        'end_date':end_date
        
    })
    
    
    
    return HttpResponse(t.render(c))

def convert_to_date(param_date):
    return datetime(*time.strptime(param_date, "%Y-%m-%d")[:6])
    
