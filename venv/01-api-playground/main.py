import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_data():
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return []


def process_data(posts):
    # Take first 5 posts
    return posts[:5]


def display_data(posts):
    for post in posts:
        print("\n------------------------")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")


def save_to_file(posts):
    with open("output.json", "w") as file:
        json.dump(posts, file, indent=4)


def main():
    data = fetch_data()
    processed = process_data(data)
    display_data(processed)
    save_to_file(processed)


if __name__ == "__main__":
    main()