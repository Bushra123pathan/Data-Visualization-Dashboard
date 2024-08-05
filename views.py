# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SalesData
import plotly.express as px
import pandas as pd
import csv
import random
from datetime import datetime, timedelta
from dashboard.models import SalesData

def dashboard_view(request):
    data = SalesData.objects.all()
    df = pd.DataFrame(list(data.values()))
    
    # Plotly charts
    fig = px.bar(df, x='date', y='sales_amount', color='category')
    graph = fig.to_html(full_html=False)
    
    return render(request, 'dashboard/dashboard.html', {'graph': graph, 'data': data})
@login_required
def dashboard_view(request):
    # Fetch all sales data from the database
    data = SalesData.objects.all()

    # Convert data to a DataFrame for easier manipulation with Pandas and Plotly
    df = pd.DataFrame(list(data.values()))

    # Create a bar chart using Plotly
    bar_chart = px.bar(
        df, 
        x='date', 
        y='sales_amount', 
        color='category', 
        title='Sales Amount by Category over Time',
        labels={'sales_amount': 'Sales Amount', 'date': 'Date'},
        template='plotly_dark'
    )

    # Create a line chart using Plotly
    line_chart = px.line(
        df, 
        x='date', 
        y='sales_amount', 
        color='category', 
        title='Sales Trend over Time',
        labels={'sales_amount': 'Sales Amount', 'date': 'Date'},
        template='plotly_dark'
    )

    # Convert charts to HTML to be rendered in the template
    bar_chart_html = bar_chart.to_html(full_html=False)
    line_chart_html = line_chart.to_html(full_html=False)

    # Render the dashboard template with the charts and data
    return render(request, 'dashboard/dashboard.html', {
        'bar_chart': bar_chart_html,
        'line_chart': line_chart_html,
        'data': data,
    })

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