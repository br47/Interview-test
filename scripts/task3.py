import csv
from operator import itemgetter

def get_value(a):
    products_list = []

    with open("../csvs/products.csv") as file_products:
        reader = csv.reader(file_products)
        for i,row in enumerate(reader):
            products_list.insert(i, [row[0], row[2]])

    products_list.pop(0)

    for product_id,price in products_list:
        if int(product_id) == a:
            return float(price)

def get_customer_prices():
    order_list = []

    with open("../csvs/orders.csv") as file_orders:
        reader = csv.reader(file_orders)
        for i,row in enumerate(reader):
            order_list.insert(i, [row[1], row[2]])

    order_list.pop(0)

    customer_total_price_list = []

    for customer_id, products_id in order_list:
        products_id = list(products_id.replace(" ", ""))
        total_price = 0
        for product_id in products_id:
            total_price += get_value(int(product_id))
        
        customer_total_price_list.append([customer_id, total_price])
    
    return customer_total_price_list

def get_customer_ranking():
    customer_list = []

    with open("../csvs/customers.csv") as file_customers:
        reader = csv.reader(file_customers)
        for i,row in enumerate(reader):
            customer_list.insert(i, [row[0], row[1], row[2]])

    customer_list.pop(0)

    customer_total_price_list = get_customer_prices()
    unique_ids = []

    for customer_id,euros in customer_total_price_list:
        if customer_id not in unique_ids:
            unique_ids.append(customer_id)

    unique_customer_total_price_list = []

    for id in unique_ids:
        customer = []
        total_euros = 0
        for customer_id,euros in customer_total_price_list:
            if id == customer_id:
                total_euros = total_euros + euros
                customer.insert(0, [customer_id, total_euros])
        unique_customer_total_price_list.append(customer[0])

    outcome_list = []
    
    for customer_id, total_price in unique_customer_total_price_list:
        for cust_id,firstname,lastname in customer_list:
            if customer_id == cust_id:
                outcome_list.append([cust_id, firstname, lastname, total_price])

    outcome_list.sort(key = itemgetter(3), reverse = True)
    outcome_list.insert(0, ["id", "first name", "last name", "total price"])
    return outcome_list

#main
outcome = get_customer_ranking()
print(outcome)
with open("../outcome_csvs/customer_ranking.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(outcome)