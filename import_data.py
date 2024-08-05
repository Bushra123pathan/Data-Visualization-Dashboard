import csv
import random
from datetime import datetime, timedelta
from dashboard.models import SalesData

def import_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            SalesData.objects.create(
                date=datetime.strptime(row[0], '%Y-%m-%d'),
                category=row[1],
                sales_amount=float(row[2])
            )

def generate_random_data():
    categories = ['Electronics', 'Books', 'Clothing', 'Food']
    start_date = datetime.now() - timedelta(days=365)
    for _ in range(1000):
        date = start_date + timedelta(days=random.randint(0, 365))
        category = random.choice(categories)
        sales_amount = random.uniform(100, 5000)
        SalesData.objects.create(date=date, category=category, sales_amount=sales_amount)