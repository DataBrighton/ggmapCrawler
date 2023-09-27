import json

list_HN = ['Hoàn Kiếm', 'Đống Đa', 'Ba Đình', 'Hai Bà Trưng', 'Hoàng Mai','Thanh Xuân',
           'Long Biên', 'Nam Từ Liêm', 'Bắc Từ Liêm', 'Tây Hồ', 'Cầu Giấy', 'Hà Đông',
           'Sơn Tây', 'Ba Vì', 'Chương Mỹ', 'Phúc Thọ', 'Đan Phượng', 'Đông Anh', 
           'Gia Lâm', 'Hoài Đức', 'Mê Linh', 'Mỹ Đức', 'Phú Xuyên', 'Quốc Oai', 
           'Sóc Sơn', 'Thạch Thất', 'Thanh Oai', 'Thường Tín', 'Ứng Hòa', 'Thanh Trì']
select = ["title", "link", "main_category", "rating", "reviews",  "website", "phone" , "address"]

queries = []
for item in list_HN:
    keyword = f'siêu thị ở {item}'
    query = {'keyword': keyword,
             'select': select}
    queries.append(query)

path = 'D:\google-maps-scraper\src\query_sieuthiHN.json'
# with open(path, 'w', encoding='utf8') as f:
#     json.dump(queries, f, ensure_ascii=False)
with open(path, encoding='utf-8') as f:
    data = json.load(f)
print(data)
