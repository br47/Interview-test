import csv

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

def get_prices():
    order_list = []

    with open("../csvs/orders.csv") as file_orders:
        reader = csv.reader(file_orders)
        for i,row in enumerate(reader):
            order_list.insert(i, [row[0], row[2]])

    order_list.pop(0)
    outcome_list = []

    for order_id, products_id in order_list:
        products_id = list(products_id.replace(" ", ""))
        total_price = 0
        for product_id in products_id:
            total_price += get_value(int(product_id))
        
        outcome_list.append([order_id, total_price])
    
    outcome_list.insert(0, ["id", "total price"])
    return outcome_list

#main
outcome = get_prices()
print(outcome)
with open("../outcome_csvs/order_prices.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(outcome)