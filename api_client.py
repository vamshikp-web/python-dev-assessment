import requests

def fetch_and_display_users(num_users):
    url = f"https://jsonplaceholder.typicode.com/users"
    try:
        #Make GET request
        response = requests.get(url, timeout=10)

        # Check HTTP status
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None
        #Parse JSON
        users = response.json()

        # Validate JSON structure
        if not isinstance(users, list):
            print("Error: Unexpected JSON structure(expected a list).")
            return None

    except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    print(f"Displaying first {num_users} users:")

    count = 0
    for user in users:
        if count >= num_users:
            break

    try:
        name = user["name"]
        email = user["email"]
        city = user["address"]["city"]
        print(f"Name: {name}, Email: {email}, City: {city}")
        print("-" * 30)

        count += 1
    except KeyError:
        print("Error: Missing expected fields in user data.")
#---test Calls---

fetch_and_display_users(4)
fetch_and_display_users(16)

