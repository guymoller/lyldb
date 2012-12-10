from django.db import models
from datetime import date
from django.utils.datetime_safe import strftime



class SalesFlatOrder(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=96, blank=True)
    status = models.CharField(max_length=96, blank=True)
    coupon_code = models.CharField(max_length=765, blank=True)
    customer_id = models.IntegerField(null=True, blank=True)
    discount_amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    discount_canceled = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    discount_invoiced = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    discount_refunded = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    grand_total = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    shipping_amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    shipping_canceled = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    shipping_invoiced = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    shipping_refunded = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    shipping_tax_amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    shipping_tax_refunded = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    subtotal = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    subtotal_canceled = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    subtotal_invoiced = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    subtotal_refunded = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    tax_amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    tax_canceled = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    tax_invoiced = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    tax_refunded = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    total_canceled = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    total_invoiced = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    total_qty_ordered = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    total_refunded = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    email_sent = models.IntegerField(null=True, blank=True)
    gift_message_id = models.IntegerField(null=True, blank=True)
    quote_address_id = models.IntegerField(null=True, blank=True)
    quote_id = models.IntegerField(null=True, blank=True)
    shipping_address_id = models.IntegerField(null=True, blank=True)
    base_adjustment_negative = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    base_adjustment_positive = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    base_shipping_discount_amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    base_subtotal_incl_tax = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    base_total_due = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    shipping_discount_amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    subtotal_incl_tax = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    total_due = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    customer_dob = models.DateTimeField(null=True, blank=True)
    increment_id = models.CharField(max_length=150, blank=True)
    applied_rule_ids = models.CharField(max_length=765, blank=True)
    base_currency_code = models.CharField(max_length=9, blank=True)
    customer_email = models.CharField(max_length=765, blank=True)
    customer_firstname = models.CharField(max_length=765, blank=True)
    customer_lastname = models.CharField(max_length=765, blank=True)
    customer_middlename = models.CharField(max_length=765, blank=True)
    customer_prefix = models.CharField(max_length=765, blank=True)
    customer_suffix = models.CharField(max_length=765, blank=True)
    discount_description = models.CharField(max_length=765, blank=True)
    order_currency_code = models.CharField(max_length=765, blank=True)
    original_increment_id = models.CharField(max_length=150, blank=True)
    remote_ip = models.CharField(max_length=765, blank=True)
    shipping_method = models.CharField(max_length=765, blank=True)
    x_forwarded_for = models.CharField(max_length=765, blank=True)
    customer_note = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    total_item_count = models.IntegerField()
    customer_gender = models.IntegerField(null=True, blank=True)
    base_shipping_incl_tax = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    
   
    class Meta:
        db_table = u'sales_flat_order'


class SalesFlatOrderItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(SalesFlatOrder)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    product_id = models.IntegerField(null=True, blank=True)
    sku = models.CharField(max_length=765, blank=True)
    name = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    qty_shipped = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    base_cost = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=4)
    base_price = models.DecimalField(max_digits=14, decimal_places=4)
    class Meta:
        db_table = u'sales_flat_order_item'




