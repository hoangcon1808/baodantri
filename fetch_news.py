import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

# Danh sách các chủ đề bạn muốn lấy
CATEGORIES = {
    "Trang chủ": "https://dantri.com.vn",
    "Xã hội": "https://dantri.com.vn/xa-hoi.htm",
    "Kinh doanh": "https://dantri.com.vn/kinh-doanh.htm",
    "Sức khỏe": "https://dantri.com.vn/suc-khoe.htm"
}

BASE_URL = "https://dantri.com.vn"

def fetch_multiple_categories():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'vi-VN,vi;q=0.9',
    }
    
    all_news = []
    seen_links = set() # Bộ lọc để tránh lấy trùng 1 bài báo

    for category_name, url in CATEGORIES.items():
        print(f"⏳ Đang quét chuyên mục: {category_name}...")
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status() 
            response.encoding = 'utf-8'
        except Exception as e:
            print(f"❌ Lỗi khi tải {category_name}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')
        
        for article in articles:
            title_tag = article.find(['h2', 'h3'])
            if not title_tag: continue
                
            a_tag = title_tag.find('a')
            if not a_tag: continue
                
            title = a_tag.text.strip()
            link = a_tag.get('href')
            
            if link and link.startswith('/'):
                link = urljoin(BASE_URL, link)
                
            excerpt_tag = article.find('div', class_='article-excerpt')
            summary = excerpt_tag.text.strip() if excerpt_tag else ""
            
            # Chỉ lấy bài nếu link này chưa từng được lưu
            if title and link and (link not in seen_links):
                seen_links.add(link)
                all_news.append({
                    "category": category_name, 
                    "title": title,
                    "link": link,
                    "published": "Mới cập nhật", 
                    "summary": summary
                })

    return all_news

if __name__ == "__main__":
    news_data = fetch_multiple_categories()
    
    if news_data:
        # Lưu toàn bộ ra 1 file JSON
        with open("dantri_news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, ensure_ascii=False, indent=4)
        print(f"✅ Hoàn tất! Đã lưu tổng cộng {len(news_data)} bài viết vào dantri_news.json.")
    else:
        print("❌ Không có dữ liệu nào được lấy.")
