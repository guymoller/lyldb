# Create your views here.
from django.http import HttpResponse
from django.template.context import Context
from django.template import loader
from models import SalesFlatOrder
from datetime import date, timedelta,datetime
import time
from itertools import groupby
from django.utils.datetime_safe import strftime
from django.db.models import Sum

def index(request):
    """
    parameteres: start, end expect the format yyyy-mm-dd, range_label - 30d, 7d, MTD etc
    """
    res = request.GET.get('res')
    if res is None: res = "day"
    def date_format(res):
        config = {"day":"%d-%m-%Y", "week":"%W","month":"%m-%Y" }
        return config.get(res)


    today = datetime.now()  
    t = loader.get_template('db/index.html')
    if request.GET.get('start'): 
        start_date = convert_to_date(request.GET.get('start'))
    else:
        start_date = today + timedelta(days=-30) #30 days 
    if request.GET.get('end'):
        end_date=convert_to_date(request.GET.get('end'))
    else:
        end_date = today
    orders = SalesFlatOrder.objects.filter(created_at__gte = start_date).filter(created_at__lte = end_date).order_by('created_at')
    order_stats = {'count':len(orders), 'sum': orders.aggregate(Sum('grand_total'))['grand_total__sum']}
    today_orders = SalesFlatOrder.objects.filter(created_at__gte = datetime(today.year, today.month, today.day))
    today_revenues = today_orders.aggregate(Sum('grand_total'))['grand_total__sum']
    orders_by_date = []
    
    for day, order_group in groupby(orders,lambda o: strftime(o.created_at, date_format(res))):
        orders_by_date.append ({'day':day, 'display_date': day.replace('-','.')[:-5],  'orders': list(order_group)})
        
    for row in orders_by_date:
        
        row['revenues']= sum([x.grand_total for x  in row['orders']])
        row['count'] = len(row['orders'])
    
    orders_by_date_reverse = orders_by_date[:]
    orders_by_date_reverse.reverse()
    c = Context({
        'orders': orders,
        'order_stats':order_stats,
        'orders_by_date':orders_by_date,  
        'orders_by_date_reverse':orders_by_date_reverse,            
        'start_date':start_date,
        'end_date':end_date,
        'date_range_links':date_range_links(request.GET.get('range_label')),
        'res':res,
        'resolutions':['day','week','month'],
        'range_label':request.GET.get('range_label'),
        'today_orders':{'count':len(today_orders),'sum':today_revenues}
        
    })
    
    
    
    return HttpResponse(t.render(c))

def convert_to_date(param_date):
    return datetime(*time.strptime(param_date, "%Y-%m-%d")[:6])

def convert_to_string(p_date):
    return strftime(p_date, "%Y-%m-%d")
    
def date_range_links(p_label = '30d'):
    """
    generates date ranges for the query
     [{'label': '7d',  'range':{'start':'2011-11-01','end':'2011-11-07'}},
      {'label': '30d', 'range':{'start':'2011-11-01','end':'2011-11-30'}}] end is always today
    """
    if p_label is None: p_label = '30d'
    # first calculate timedeltas for YTD, MTD
    res = []
    today = datetime.now()
    res.append({
        'label':'7d', 
        'range':{
                'start':convert_to_string(today+timedelta(days=-7)),
                'end':convert_to_string(today)
                }})
    res.append({
        'label':'30d', 
        'range':{
                'start':convert_to_string(today+timedelta(days=-30)),
                'end':convert_to_string(today)
                }})
    res.append({
        'label':'MTD', 
        'range':{
                'start':convert_to_string(datetime(today.year,today.month,1)),
                'end':convert_to_string(today)
                }})
    res.append({
        'label':'YTD', 
        'range':{
                'start':convert_to_string(datetime(today.year,1,11)),
                'end':convert_to_string(today)
                }})
    for l in res:
        if l['label'] == p_label:
            l['active'] = True
        else:
            l['active'] = False

    return res
    
    





