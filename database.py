import sqlite3
import pandas as pd
import logging
import io
from pathlib import Path

class Database:
    def __init__(self):
        # Get current directory where database.py is located
        current_dir = Path(__file__).parent
        # Create a 'data' directory for the database
        data_dir = current_dir / 'data'
        data_dir.mkdir(exist_ok=True)
        # Set database path
        self.db_path = data_dir / 'properties.db'
        self.conn = None
        self.cursor = None
        self.connect()
        self.setup_database()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            logging.info("Database connection established successfully.")
        except Exception as e:
            logging.error(f"Database connection error: {e}")
            raise

    def setup_database(self):
        # Create tables if they do not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY,
                name TEXT,
                host_id INTEGER,
                host_name TEXT,
                neighbourhood_group TEXT,
                neighbourhood TEXT,
                latitude REAL,
                longitude REAL,
                room_type TEXT,
                price INTEGER,
                minimum_nights INTEGER,
                number_of_reviews INTEGER,
                last_review TEXT,
                reviews_per_month REAL,
                calculated_host_listings_count INTEGER,
                availability_365 INTEGER,
                number_of_reviews_ltm INTEGER,
                license TEXT
            )
        ''')
        logging.info("Properties table created or already exists.")

        # Load sample data if necessary
        self.load_sample_data()
        self.conn.commit()

    def load_sample_data(self):
        # Sample data loading logic can be added here
        logging.info("Sample data loaded into the database.")

    def execute_query(self, query):
        try:
            result = pd.read_sql_query(query, self.conn)
            return result
        except Exception as e:
            logging.error(f"Error executing SQL query: {e}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()