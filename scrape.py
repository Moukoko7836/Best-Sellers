import requests
from bs4 import BeautifulSoup
from jinja2 import Template
import os

# 1) Your Amazon affiliate tag goes here:
affiliate_tag = "moukoko7836-21"  # replace YOURTAG-21 with your real tag

# 2) Where to get Best-Sellers (UK example):
url = "https://www.amazon.co.uk/gp/bestsellers"

# 3) Grab the page:
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
resp.raise_for_status()

# 4) Find top 10 items:
soup = BeautifulSoup(resp.text, "html.parser")
items = []
for div in soup.select(".zg-item-immersion")[:10]:
    title = div.select_one(".p13n-sc-truncate").get_text(strip=True)
    link = "https://www.amazon.co.uk" + div.select_one("a")['href']
    # add your affiliate tag:
    link = link + ("?tag=" + affiliate_tag)
    items.append({"title": title, "link": link})

# 5) Load our HTML template:
with open("template.html") as f:
    tpl = Template(f.read())

# 6) Render the final page:
output = tpl.render(items=items)

# 7) Save it as index.html:
with open("index.html", "w") as f:
    f.write(output)

print("✅ index.html created with top items!")