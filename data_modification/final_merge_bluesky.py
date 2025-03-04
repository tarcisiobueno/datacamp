import json
json_files = ["combined_top_posts.json", "combined_top_posts_new.json", "combined_top_posts_sports.json"]
merged_file = "merged_posts.json"

def merge_json_files(files, output_file):
    """Merge multiple JSON files into one, sorting by likes."""
    merged_data = []
    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                merged_data.extend(data)
        except FileNotFoundError:
            print(f"Warning: {file} not found. Skipping...")
        except json.JSONDecodeError:
            print(f"Error: {file} is not a valid JSON file. Skipping...")
    merged_data = sorted(merged_data, key=lambda x: x.get("likes", 0), reverse=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)

    print(f"Merged {len(merged_data)} posts from {len(files)} files into {output_file}")
merge_json_files(json_files, merged_file)
