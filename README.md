# Data-Visualization-Dashboard

# Data Visualization Dashboard

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Configure the database in `settings.py`.

3. Run migrations:
    ```bash
    python manage.py migrate
    ```

4. Import or generate data:
    ```bash
    python manage.py shell
    >>> from dashboard import data_import
    >>> data_import.generate_random_data()
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the dashboard at `http://localhost:8000/dashboard`.

## Features

- User authentication
- Real-time data visualization with Plotly
- Data filtering by date range or category
