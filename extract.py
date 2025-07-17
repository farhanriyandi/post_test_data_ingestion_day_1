# # ekstrak: https://api.ekraf.go.id/posts
import requests
import csv

POSTS_URL = "https://api.ekraf.go.id/posts"

def fetch_api_data():
    print("Fetching data from {}...".format(POSTS_URL))
    try:
        print("Fetching data")
        response = requests.get(POSTS_URL, timeout=10)
        print(response, "Ini response")
        response_json = response.json()
        print("Top-level keys:", response_json.keys())

        # Ambil bagian list dari key "data"
        data = response_json.get("data", [])

        # cek apakah data adalah list dan tidak kosong
        if not isinstance(data, list) or len(data) == 0:
            print("Data kosong atau bukan list")
            return
        
        print("First Post:", data[0])

        # Ambil header dari dict pertama
        headers = data[0].keys()
        # print("Headers:", headers)

        # masukin ke csv, db, atau apapun
        print("Data fetched successfully.")

        # write to csv
        with open("posts_ekraf.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print("Data written to 'posts_ekraf.csv' successfully.")

    except Exception as e:
        print("Error fetching data from API: {}".repr(e))


fetch_api_data()

# with open("write_posts.csv", mode='r', newline='', encoding='utf-8') as infile:
#     reader = csv.DictReader(infile)
#     data = list(reader)

#     print("Data from csv:", data)
#     print("first row:", data[0])