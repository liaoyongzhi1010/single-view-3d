from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import os
import time

# 设置无头浏览器
options = Options()
options.add_argument("--headless")  # 无界面模式
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# 启动浏览器（确保 chromedriver 在 PATH 中）
driver = webdriver.Chrome(options=options)
driver.get("https://3dvconf.github.io/2024/accepted-papers/")

# 等待页面渲染（可按需调大）
time.sleep(3)

# 获取完整 HTML
html = driver.page_source
driver.quit()

# 用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, "html.parser")
paper_elements = soup.find_all("a", class_="paper_a")

# 抽取标题和摘要
papers = []
for a in paper_elements:
    title_tag = a.find("span", class_="paper_title")
    abstract_tag = a.find("div", class_="paper_abstract")
    if title_tag and abstract_tag:
        title = title_tag.get_text(strip=True)
        abstract = abstract_tag.get_text(strip=True)
        papers.append({"title": title, "abstract": abstract})

# 保存到 JSON（保存在当前目录）
output_path = os.path.join(os.path.dirname(__file__), "3dv2024_papers.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)

print(f"共提取 {len(papers)} 篇论文，已保存至 {output_path}")
