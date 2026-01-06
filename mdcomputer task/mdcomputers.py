import json
import os
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, urljoin

URL="https://mdcomputers.in/"
OUTPUT_FILE="products.json"



def soup_from_url(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

def load():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
def save(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
def extract(soup,seen_urls,all_products):
    for item in soup.select("div.product-grid-item"):
        title=item.select_one("h3.product-entities-title a")
        price=item.select_one("span.price")
        if not title:
            continue
        url =urljoin(URL,title["href"])
        if url in seen_urls:
            continue
        product={
            "title":title.get_text(strip=True),
            "url":url,
            "price":None,
            "deleted_price":None,
        }  
        if price:
            ins=price.select_one("span.ins")
            del_=price.select_one("span.del")
            product["price"]=ins.get_text(strip=True) if ins else price.get_text(strip=True)
            product["deleted_price"]=del_.get_text(strip=True) if del_ else None
        all_products.append(product)
        seen_urls.add(url)
        save(all_products)
        print(f"{len(all_products)} products saved")   
def get_total_pages(soup):
    footer_text = soup.get_text(" ", strip=True)
    match = re.search(r"\((\d+)\s+Pages?\)", footer_text)

    if match:
        return int(match.group(1))
    return 1        
def scrape(input_term):
   search_url = f"{URL}?route=product/search&search={quote_plus(input_term)}" 
   all_products=load()
   seen_urls={product["url"] for product in all_products}
   soup=soup_from_url(search_url)
   total_pages=get_total_pages(soup)
   print(f"{total_pages} pages found")
   extract(soup,seen_urls,all_products)
   for page in range(2,total_pages+1):
       page_url=f"{search_url}&page={page}"
       print(f"\nFetching page {page}: {page_url}")
       soup=soup_from_url(page_url)
       extract(soup,seen_urls,all_products)
       time.sleep(1)  
   print(f"Scraping completed. {len(all_products)} products found.")  

if __name__=="__main__":
    term=input("Enter search term: ").strip()
    scrape(term)    