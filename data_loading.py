import requests
import pandas as pd

# Fetch the data from the API (URL given on the website)
url = "https://api.exactpark.com/api/v2/arlington/status/zones"
response = requests.get(url)

# Make sure the API fetch request was successful (200 = OK)
if response.status_code == 200:
    data = response.json()
else:
    print("Error:", response.status_code)

# Convert the JSON data to a DataFrame
if 'data' in data:
    df = pd.json_normalize(data['data'])  # Use json_normalize to flatten the nested structure
else:
    print("No data found in the response.")

# Convert and Save to CSV to export and push to GitHub
df.to_csv('data/parking_stall_status.csv', index=False)

# Print the information of the dataset
print(df.info())
print(df.head(5))
print(df.tail(5))
