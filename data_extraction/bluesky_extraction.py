import requests
import json
import time
import os

# List of websites and their Bluesky handles
WEBSITES = [ "theintercept.com", "vice.com", "buzzfeed.com", "forbes.com",
    "politico.com", "huffpost.com", "theatlantic.com", "rollingstone.com",
    "vanityfair.com"]

DID_URL_TEMPLATE = "https://public.api.bsky.app/xrpc/com.atproto.identity.resolveHandle?handle={}"
FEED_URL_TEMPLATE = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor={did}&limit=100&cursor={cursor}"

# Configurations
TOTAL_POSTS_TO_FETCH = 2000  
TOP_N = 1000  
COMBINED_JSON_FILE = "combined_top_posts_new.json"  

def get_did(username):
    """Fetch the DID for a given Bluesky username."""
    response = requests.get(DID_URL_TEMPLATE.format(username))
    if response.status_code == 200:
        return response.json().get("did")
    else:
        print(f"Error fetching DID for {username}: {response.text}")
        return None


def get_posts(did, total_posts=TOTAL_POSTS_TO_FETCH):
    """Fetch posts from a Bluesky user's feed with pagination."""
    all_posts = []
    cursor = None  
    while len(all_posts) < total_posts:
        try:
            url = FEED_URL_TEMPLATE.format(did=did, cursor=cursor or "")
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Error fetching posts for DID {did}: {response.text}")
                break
            data = response.json()
            posts = data.get("feed", [])
            if not posts:
                print("No more posts found.")
                break
            all_posts.extend(posts)
            cursor = data.get("cursor")
            if not cursor:
                break 
            print(f"Fetched {len(all_posts)} posts so far for {did}...")

            # Sleep to avoid rate limits
            time.sleep(1.5)

        except Exception as e:
            print(f"Error fetching posts: {e}")
            break

    return all_posts


def process_website(username):
    """Fetch and process posts for a given Bluesky username."""
    did = get_did(username)

    if not did:
        return []

    print(f"Found DID for {username}: {did}")
    posts = get_posts(did)
    extracted_posts = []
    for post in posts:
        post_data = post.get("post", {})
        if "record" in post_data:
            extracted_posts.append({
                "website": username,  # Add source website
                "text": post_data["record"].get("text", ""),
                "likes": post_data.get("likeCount", 0),
                "reposts": post_data.get("repostCount", 0),
                "replies": post_data.get("replyCount", 0),
                "quotes": post_data.get("quoteCount", 0),
                "total_engagement": post_data.get("likeCount", 0) +
                                    post_data.get("repostCount", 0) +
                                    post_data.get("replyCount", 0) +
                                    post_data.get("quoteCount", 0),
                "created_at": post_data["record"].get("createdAt", ""),
            })

    sorted_posts = sorted(extracted_posts, key=lambda x: x["likes"], reverse=True)
    top_posts = sorted_posts[:TOP_N]
    with open(f"{username}_top_{TOP_N}_posts.json", "w", encoding="utf-8") as f:
        json.dump(top_posts, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(top_posts)} most liked posts for {username} to JSON.")
    return top_posts 


def combine_json_files():
    """Combine all individual JSON files into one."""
    combined_data = []
    for website in WEBSITES:
        filename = f"{website}_top_{TOP_N}_posts.json"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                website_data = json.load(f)
                combined_data.extend(website_data)
    combined_data = sorted(combined_data, key=lambda x: x["likes"], reverse=True)
    with open(COMBINED_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=4, ensure_ascii=False)

    print(f" Combined {len(combined_data)} posts from all sources into {COMBINED_JSON_FILE}.")

all_posts = []
for website in WEBSITES:
    print(f"Processing {website}...")
    all_posts.extend(process_website(website))

combine_json_files()
print("Data collection and merging complete!")
