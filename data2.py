import requests
import matplotlib.pyplot as plt

# Define the base URL for JSONPlaceholder API
base_url = 'https://jsonplaceholder.typicode.com/'

# Specify the ID of the post you want to retrieve (replace with the desired post ID)
post_id = 1

# Make a GET request to retrieve the specific post
response = requests.get(base_url + f'posts/{post_id}')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    post = response.json()
    
    # Prepare data for the table
    data = [['Attribute', 'Value']]
    for key, value in post.items():
        data.append([key, value])

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis('off')
    
    # Create the table
    table = plt.table(cellText=data, loc='center', cellLoc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    
    plt.title(f'Post ID: {post_id}')
    plt.show()

else:
    # Print an error message if the request was not successful
    print(f'Error: Unable to retrieve data. Status code {response.status_code}')
