import requests
import matplotlib.pyplot as plt

# Define the base URL for JSONPlaceholder API
base_url = 'https://jsonplaceholder.typicode.com/'

# Make a GET request to retrieve a list of posts
response = requests.get(base_url + 'posts')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    posts = response.json()
    
    # Prepare data for table
    data = [['UserId', 'Id', 'Title', 'Body']]
    for post in posts:
        data.append([post['userId'], post['id'], post['title'], post['body']])

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis('off')
    
    # Create the table
    table = plt.table(cellText=data, loc='center', cellLoc = 'center')
    table.auto_set_font_size(True)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    
    plt.show()

else:
    # Print an error message if the request was not successful
    print(f'Error: Unable to retrieve data. Status code {response.status_code}')
