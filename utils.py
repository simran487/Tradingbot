import csv
from datetime import datetime

def save_order_to_csv(order_data, filename="orders.csv"):
    keys = ['symbol', 'side', 'type', 'price', 'origQty', 'status', 'updateTime']
    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'symbol': order_data.get('symbol'),
            'side': order_data.get('side'),
            'type': order_data.get('type'),
            'price': order_data.get('price'),
            'origQty': order_data.get('origQty'),
            'status': order_data.get('status'),
            'updateTime': datetime.now()
        })
