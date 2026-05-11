import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

# URL Trang chủ Dân Trí
URL = "https://dantri.com.vn"

def fetch_dantri_homepage():
    # Giả lập trình duyệt để tránh bị chặn
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'vi-VN,vi;q=0.9',
    }
    
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        response.raise_for_status() # Báo lỗi nếu tải trang thất bại
        response.encoding = 'utf-8'
    except Exception as e:
        print(f"❌ Lỗi khi kết nối đến trang chủ: {e}")
        return []

    # Phân tích mã nguồn HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = []

    # Dân Trí bọc các bài báo trong thẻ <article>
    articles = soup.find_all('article')
    
    for article in articles:
        # Lấy thẻ tiêu đề (thường là h2 hoặc h3)
        title_tag = article.find(['h2', 'h3'])
        if not title_tag: 
            continue
            
        a_tag = title_tag.find('a')
        if not a_tag: 
            continue
            
        title = a_tag.text.strip()
        link = a_tag.get('href')
        
        # Nối link nếu link bị thiếu phần domain (dạng /xa-hoi/...)
        if link and link.startswith('/'):
            link = urljoin(URL, link)
            
        # Lấy phần tóm tắt
        excerpt_tag = article.find('div', class_='article-excerpt')
        summary = excerpt_tag.text.strip() if excerpt_tag else ""
        
        # Lọc bỏ các bài không hợp lệ và kiểm tra trùng lặp
        if title and link:
            if not any(item['link'] == link for item in news_list):
                news_list.append({
                    "title": title,
                    "link": link,
                    "published": "Mới cập nhật", 
                    "summary": summary
                })

    return news_list

if __name__ == "__main__":
    news_data = fetch_dantri_homepage()
    
    if news_data:
        # Lưu ra file JSON
        with open("dantri_news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, ensure_ascii=False, indent=4)
        print(f"✅ Đã quét và lưu {len(news_data)} bài viết từ trang chủ.")
    else:
        print("❌ Không có dữ liệu nào được lấy.")
