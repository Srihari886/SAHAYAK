import csv
import os
from datetime import datetime

LOG_FILE = "logs.csv"

def log_query(category, query):

    exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not exists:
            writer.writerow([
                "Timestamp",
                "Category",
                "Query"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            category,
            query
        ])