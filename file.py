# import requests
# import json

# # Load JSON file
# with open('data.json') as f:
#     data = json.load(f)

# # Iterate through each item in the JSON file and post it to the API
# for item in data:
#     r = requests.post("https://estadiosapi.vercel.app/api/v1/teams/", json=item)
#     if r.status_code == 201:  # Assuming 201 means successful creation
#         print(f"Item {item} posted successfully.")
#     else:
#         print(f"Failed to post item {item}. Status code: {r.status_code}")


import requests

# Send a DELETE request to the API endpoint
r = requests.delete("https://estadiosapi.vercel.app/api/v1/teams/")

# Check if the deletion was successful
if r.status_code == 204:  # Assuming 204 means successful deletion
    print("All contents of the API have been deleted.")
else:
    print(f"Failed to delete contents of the API. Status code: {r.status_code}")
