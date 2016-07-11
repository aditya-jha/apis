from users.serializers.buyer import serialize_buyer
from ..models.order import OrderStatus, OrderPaymentStatus
from ..models.subOrder import filterSubOrder
from ..models.payments import filterBuyerPayment
from .subOrder import serializeSubOrder, parseSubOrders
from .payments import serializeBuyerPayment, parseBuyerPayments

def serializeOrder(orderEntry, parameters = {}):
	order = {}
	order["orderID"]=orderEntry.id	
	order["product_count"]=orderEntry.product_count
	order["retail_price"]=orderEntry.retail_price
	order["calculated_price"]=orderEntry.calculated_price
	order["edited_price"]=orderEntry.edited_price
	order["cod_charge"]=orderEntry.cod_charge
	order["shipping_charge"]=orderEntry.shipping_charge
	order["final_price"]=orderEntry.final_price	
	order["display_number"]=orderEntry.display_number
	order["remarks"]=orderEntry.remarks
	order["created_at"]=orderEntry.created_at
	order["updated_at"]=orderEntry.updated_at

	order["order_status"] = {
		"value": orderEntry.order_status,
		"display_value":OrderStatus[orderEntry.order_status]["display_value"]
	}

	order["order_payment_status"]= {
		"value": orderEntry.order_payment_status,
		"display_value":OrderPaymentStatus[orderEntry.order_payment_status]["display_value"]
	}

	if "sub_order_details" in parameters and parameters["sub_order_details"] == 1:
		subOrderQuerySet = filterSubOrder(parameters)
		subOrderQuerySet = subOrderQuerySet.filter(order_id = orderEntry.id)
		order["sub_orders"] = parseSubOrders(subOrderQuerySet,parameters)

	if "buyer_payment_details" in parameters and parameters["buyer_payment_details"] == 1:
		buyerPaymentQuerySet = filterBuyerPayment(parameters)
		buyerPaymentQuerySet = buyerPaymentQuerySet.filter(order_id = orderEntry.id)
		order["buyer_payments"] = parseBuyerPayments(buyerPaymentQuerySet,parameters)

	if "buyer_details" in parameters and parameters["buyer_details"] == 1:
		order["buyer"]=serialize_buyer(orderEntry.buyer, parameters)
	else:
		buyer = {}
		buyer["buyerID"] = orderEntry.buyer.id
		buyer["name"] = orderEntry.buyer.name
		order["buyer"] = buyer
	
	return order

def parseOrders(OrderQuerySet, parameters = {}):

	Orders = []

	for Order in OrderQuerySet:
		OrderEntry = serializeOrder(Order, parameters)
		Orders.append(OrderEntry)

	return Orders