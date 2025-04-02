import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker for realistic data
fake = Faker()

# Set random seed for reproducibility
np.random.seed(42)

# Define parameters
num_tickets = 500
start_date = datetime(2024, 3, 1, 8, 0, 0)  # Start on March 29, 2024, 8 AM
end_date = datetime(2025, 3, 30, 23, 59, 59)  # End on March 30, 2025, 11:59 PM

# Categories and severities
categories = ['Hardware', 'Software', 'Network', 'Security']
severities = ['Low', 'Medium', 'High']
teams = ['TeamA', 'TeamB', 'TeamC']


# Function to generate random datetime within range
def random_datetime(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

# Generate initial data
data = {
    'TicketID': [f'T{str(i).zfill(3)}' for i in range(1, num_tickets + 1)],
    'CreatedDate': [random_datetime(start_date, end_date) for _ in range(num_tickets)],
    'Category': [random.choice(categories) for _ in range(num_tickets)],
    'Severity': [random.choice(severities) for _ in range(num_tickets)],
    'ShotsTaken': [random.randint(1, 10) for _ in range(num_tickets)],
     'SLA_Hours': [24 if random.choice(severities) == 'High' else 48 for _ in range(num_tickets)],
    'Team': [random.choice(teams) for _ in range(num_tickets)],
}
# Create DataFrame
df = pd.DataFrame(data)

# Add ResolvedDate (60% resolved, 40% unresolved)
df['ResolvedDate'] = df['CreatedDate'].apply(
    lambda x: x + timedelta(hours=random.randint(1, 48)) if random.random() < 0.6 else None
)

# Add Status (Resolved, Open, Escalated)
df['Status'] = df.apply(
    lambda row: 'Resolved' if pd.notnull(row['ResolvedDate']) 
    else 'Escalated' if random.random() < 0.5 else 'Open',
    axis=1
)

# Add FirstContactResolved (60% Yes for resolved tickets)
df['FirstContactResolved'] = df.apply(
    lambda row: random.choice(['Yes', 'No']) if row['Status'] == 'Resolved' and random.random() < 0.6 else 'No',
    axis=1
)

# Add CSAT (1-5 for resolved tickets only)
df['CSAT'] = df['Status'].apply(lambda x: random.randint(1, 5) if x == 'Resolved' else None)

# Sort by CreatedDate for realism
df = df.sort_values('CreatedDate').reset_index(drop=True)

# Save to CSV
df.to_csv('2IT_HelpDesk_Data.csv', index=False)
print("Dataset generated and saved as '2IT_HelpDesk_Data.csv'")
print(df.head())