import sqlite3
import csv
import os

DB_NAME = 'physio.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table for condition-to-exercise mappings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            condition TEXT NOT NULL,
            exercise TEXT NOT NULL
        )
    ''')
    
    # Create table for symptom-to-condition mappings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS symptoms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symptom TEXT NOT NULL,
            condition TEXT NOT NULL
        )
    ''')

    # Load data into exercises table if empty
    cursor.execute("SELECT COUNT(*) FROM exercises")
    if cursor.fetchone()[0] == 0 and os.path.exists("Condition_to_Exercises.csv"):
        with open('Condition_to_Exercises.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Expecting CSV with headers: condition, exercise
            data = [(row['condition'], row['exercise']) for row in reader]
            cursor.executemany("INSERT INTO exercises (condition, exercise) VALUES (?, ?)", data)
    
    # Load data into symptoms table if empty
    cursor.execute("SELECT COUNT(*) FROM symptoms")
    if cursor.fetchone()[0] == 0 and os.path.exists("Symptoms_to_Condition.csv"):
        with open('Symptoms_to_Condition.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Expecting CSV with headers: symptom, condition
            data = [(row['symptoms'], row['condition']) for row in reader]
            cursor.executemany("INSERT INTO symptoms (symptom, condition) VALUES (?, ?)", data)

    conn.commit()
    conn.close()

def get_exercises(condition):
    """
    Return a list of exercises for the given condition.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT exercise FROM exercises WHERE condition = ?", (condition,))
    exercises = [row[0] for row in cursor.fetchall()]
    conn.close()
    return exercises

def get_condition_by_symptom(symptom):
    """
    Return the condition associated with the given symptom, or None if not found.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT condition FROM symptoms WHERE symptom = ?", (symptom,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

if __name__ == "__main__":
    # Initialize the database and load CSV data
    init_db()
    
    # Test the functions
    test_condition = 'Back Pain'
    exercises = get_exercises(test_condition)
    print(f"Exercises for {test_condition}: {exercises}")
    
    test_symptom = 'neck stiffness'
    associated_condition = get_condition_by_symptom(test_symptom)
    print(f"Condition for symptom '{test_symptom}': {associated_condition}")
