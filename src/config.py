'''
Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/
'''
import json

path = 'D:\google-maps-scraper\src\query_sieuthiHN.json'
with open(path, encoding='utf-8') as f:
    queries = json.load(f)
# queries = [
#     {
#         "keyword": "nhà thuốc ở Hoàn Kiếm",
#         "select": ["title", "link", "main_category", "rating", "reviews",  "website", "phone" , "address"],
#     },]

number_of_scrapers = 16