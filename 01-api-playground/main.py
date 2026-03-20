import requests
import json
import argparse

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_data():
 try:
    response = requests.get(API_URL, timeout=10) 
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return []
 except requests.exceptions.RequestException as e:
    print("Error at fetching data ", e)
    return []

def process_data(posts, user_id= None, keyword= None, limit=5):
    if user_id:
        posts=[post for post in posts if post['userId']==user_id]
    if keyword :
        posts=[post for post in posts if keyword.lower() in post["title"].lower()]# Take first 5 posts
    return posts[:limit]


def display_data(posts):
    for post in posts:
        print("\n------------------------")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body preview : {post['body'][:50]}...")
        print(f"Body: {post['body']}")


def save_to_file(posts):
    with open("output.json", "w") as file:
        json.dump(posts, file, indent=4)

def filter_by_user(posts, userid):
    filter= [post for post in posts if post['id']==userid]
    return filter
def main():
    parser = argparse.ArgumentParser(description="API Data Processor")

    parser.add_argument("--limit", type=int, default=5, help="Number of posts")
    parser.add_argument("--user", type=int, help="Filter by userId")
    parser.add_argument("--keyword", type=str, help="Search in title")

    args = parser.parse_args()

    data = fetch_data()
    processed = process_data(data, args.user, args.keyword, args.limit)

    display_data(processed)
    save_to_file(processed)
if __name__ == "__main__":
    main()