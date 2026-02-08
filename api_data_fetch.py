import requests
import json

# Free public API
url = "https://randomuser.me/api/"

# Send GET request
response = requests.get(url)

# Check response
if response.status_code == 200:
    data = response.json()

    user = data["results"][0]

    name = user["name"]["first"]
    email = user["email"]
    country = user["location"]["country"]

    print("Name   :", name)
    print("Email  :", email)
    print("Country:", country)

    # Save data to file
    with open("user_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nData saved successfully")

else:
    print("Error fetching data")
