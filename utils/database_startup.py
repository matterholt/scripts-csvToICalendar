import csv
import sqlite3
from datetime import datetime

# === File paths ===
csv_file = 'games.csv'         # your CSV file
sqlite_db = './data/games.db'         # name of the SQLite database

def log_duplicate(date, time,field,fieldNum ):
  options = {
    "log":False
  }
  print(f"Duplicate skipped: {date}, {time}, {field}, {fieldNum}")
  if options["log"]:
    with open('skipped_duplicates.log', 'a') as log:
        log.write(f"Duplicate skipped: {date}, {time}, {field}, {fieldNum}\n")



def database_startup(csv_file_path):
  # === Connect to SQLite database (creates if it doesn't exist) ===
  conn = sqlite3.connect(sqlite_db)
  cursor = conn.cursor()

  # === Create table ===
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS games (
      date TEXT,
      time TEXT,
      field_location TEXT,
      field_number TEXT,
      home_coach TEXT,
      visitor_coach TEXT,
      division TEXT,
      UNIQUE(date, time, field_location, field_number)
  )
  ''')

  # === Read and insert CSV data ===
  with open(csv_file_path, newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:

        try:
            parsed_date = datetime.strptime(row['DATE'], "%A, %B %d, %Y").date()
        except ValueError as e:
            print(f"Date parsing error: {e} on row: {row}")
            continue  # Skip invalid rows or handle as needed

        # Check for duplicate
        cursor.execute('''
            SELECT 1 FROM games WHERE
                date = ? AND time = ? AND field_location = ? AND field_number = ?
        ''', (
            parsed_date,
            row['TIME'],
            row['FIELD LOCATION'],
            row['FIELD #']
        ))
        exists = cursor.fetchone()

        if exists:
          log_duplicate(date=parsed_date,time = row['TIME'],field =row['FIELD LOCATION'],fieldNum = row['FIELD #'])
          continue  # Skip insert


        cursor.execute('''
            INSERT OR IGNORE INTO games (date, time, field_location, field_number, home_coach, visitor_coach, division)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            parsed_date,
            row['TIME'],
            row['FIELD LOCATION'],
            row['FIELD #'],
            row['HOME COACH'],
            row['VISITOR COACH'],
            row['Division']
        ))

  # === Commit and close ===
  conn.commit()
  conn.close()

  print("CSV data imported into SQLite successfully.")
