import csv

def get_customers_of_product():
    products_list = []

    with open("../csvs/products.csv") as file_products:
        reader = csv.reader(file_products)
        for i,row in enumerate(reader):
            products_list.insert(i, row[0])

    products_list.pop(0)

    order_list = []

    with open("../csvs/orders.csv") as file_orders:
        reader = csv.reader(file_orders)
        for i,row in enumerate(reader):
            order_list.insert(i, [row[1], row[2]])

    order_list.pop(0)
    
    outcome_list = []

    for p_id in products_list:
        customer_list = ""
        for customer_id, products_id in order_list:
            index = products_id.find(p_id)
            if index >= 0:
                customer_list += customer_id + " "
        customer_list = customer_list[:-1]
        outcome_list.append([p_id, customer_list])

    outcome_list.insert(0, ["product id", "customers"])
    return outcome_list

#main
outcome = get_customers_of_product()
print(outcome)
with open("../outcome_csvs/product_customers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(outcome)

