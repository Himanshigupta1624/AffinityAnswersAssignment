# MDComputers Scraper

This repository contains a small Python program (`mdcomputers.py`) that extracts product information from mdcomputers.in for a given search term and saves the results to `products.json`.

**What it does**
- Accepts a search term from the user
- Fetches the search results pages on https://mdcomputers.in
- Parses the product list and saves each product as a JSON object with `title`, `url`, `price` and `deleted_price`

Requirements
- Python 3.8+
- Install dependencies:

```bash
pip install requests beautifulsoup4
```

Usage

1. Run the script:

```bash
python mdcomputers.py
```

2. Enter a search term when prompted (for example: `external harddrive`). The script will:
- fetch the search results page(s)
- follow pagination detected on the results
- append products to `products.json` as they are found

Output format
- `products.json` is a JSON array of objects. Each object contains:
  - `title`: product title string
  - `url`: absolute product URL on mdcomputers.in
  - `price`: current price string (if found)
  - `deleted_price`: previous/struck-through price string (if found)

Design choices (concise)
- Requests + BeautifulSoup: lightweight and well-suited for HTML parsing without a browser automation dependency.
- Incremental save: the script calls `save()` after each product is appended so partial results are preserved if interrupted.
- Deduplication: loaded `products.json` is used to build a `seen_urls` set so reruns continue without duplicating entries.
- Pagination detection: reads page text and uses a regex to extract a pattern like `(N Pages)` to determine total pages; falls back to 1 page if not found.
- Rate limiting: `time.sleep(1)` between pages to be polite to the server.
- Headers: custom `User-Agent` header to reduce risk of being blocked by simple bot filters.


Files
- `mdcomputers.py`: main scraper script
- `products.json`: output JSON file (created/updated by the script)


