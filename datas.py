import pandas as pd

# Load your dataset
df = pd.read_csv('Housing.csv')

# Sort the dataset by area in descending order
df = df.sort_values(by='area', ascending=False)

# Define a list of cities
cities = [
    "MUMBAI", "DELHI", "BENGALURU", "PUNE", "KOLKATA",
    "AHMEDABAD", "HYDERABAD", "VADODARA", "CHENNAI", "JAIPUR",
    "SURAT", "LUCKNOW", "UDAIPUR", "KANPUR", "NASHIK", "NAGPUR",
    "LUDHIANA", "COIMBATORE", "INDORE", "CHANDIGARH", "BHOPAL",
    "PATNA", "RAJKOT", "RAIPUR", "GUWAHATI", "RANCHI", "BHUBANESHWAR",
    "JAMSHEDPUR", "DEHRADUN", "AURANGABAD"
]

# Create an empty list to store assigned cities
assigned_cities = []

# Cycle through the list of cities and assign them to the dataset
for i in range(len(df)):
    city = cities[i % len(cities)]  # Cycle through the cities
    assigned_cities.append(city)

# Add the assigned cities as a new column in the dataset
df['city'] = assigned_cities

# Save the updated DataFrame back to a new CSV file
df.to_csv('Modified_Housing.csv', index=False)

# Print the updated DataFrame
print(df)
