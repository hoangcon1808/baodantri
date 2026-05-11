import urllib.request
import xml.etree.ElementTree as ET
import json

# URL RSS trang chủ của Báo Dân Trí
RSS_URL = "https://dantri.com.vn/rss/trang-chu.rss"

def fetch_dantri_news():
    # Thêm User-Agent để tránh bị máy chủ chặn
    req = urllib.request.Request(RSS_URL, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
    except Exception as e:
        print(f"Lỗi khi tải dữ liệu: {e}")
        return []

    # Phân tích dữ liệu XML
    root = ET.fromstring(xml_data)
    news_list = []

    # Lấy thông tin từng bài báo trong thẻ <item>
    for item in root.findall('./channel/item'):
        title = item.find('title').text if item.find('title') is not None else ""
        link = item.find('link').text if item.find('link') is not None else ""
        pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ""
        description = item.find('description').text if item.find('description') is not None else ""

        news_list.append({
            "title": title,
            "link": link,
            "published": pubDate,
            "summary": description
        })

    return news_list

if __name__ == "__main__":
    news_data = fetch_dantri_news()
    
    if news_data:
        # Lưu ra file JSON
        with open("dantri_news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, ensure_ascii=False, indent=4)
        print(f"✅ Đã lưu {len(news_data)} bài viết vào dantri_news.json")
    else:
        print("❌ Không có dữ liệu nào được lấy.")
