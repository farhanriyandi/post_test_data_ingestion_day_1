import csv
from ast import literal_eval

with open("posts_ekraf.csv", mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    data = list(reader)

    transformed_data = []
    for item in data:
        # Convert string representation of dict to actual dict
        try:
            user_dict = literal_eval(item.get("user", "{}"))
        except:
            user_dict = {}
        
        # Handle categories and tags which might also be string representations of lists
        try:
            categories = literal_eval(item.get("categories", "[]"))
        except:
            categories = []
            
        try:
            tags = literal_eval(item.get("tags", "[]"))
        except:
            tags = []

        transformed = {
            "id": item.get("id"),
            "title": item.get("title"),
            "slug": item.get("slug"),
            "excerpt": item.get("excerpt"),
            "thumbnail_seo": item.get("thumbnail_seo"),
            "published_at": item.get("published_at"),
            "likes": item.get("likes"),
            "views": item.get("views"),
            "user_id": item.get("user_id"),
            "user_name": user_dict.get("name"),
            "user_email": user_dict.get("email"),
            "categories": "|".join([str(c.get("title", "")) for c in categories]),
            "tags": "|".join([str(t.get("name", "")) for t in tags]),
            "views": item.get("views"),
            
        }
        transformed_data.append(transformed)

    if transformed_data:
        headers = transformed_data[0].keys()
        with open("transformed_post_ekraf.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(transformed_data)
        
        print("CSV berhasil disimpan sebagai 'transformed_post_ekraf.csv'")