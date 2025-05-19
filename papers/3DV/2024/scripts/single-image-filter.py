import json

# 使用你的 JSON 文件路径
file_path = r"F:\single-view-3d\papers\3DV\2024\3dv2024_papers.json"

# 加载 JSON 数据
with open(file_path, "r", encoding="utf-8") as file:
    papers = json.load(file)

# 筛选关键词
keywords = [
    "single view", "single-view", "monocular", "few-shot", "few view",
    "one image", "one view", "single image", "from an image", "monocular depth",
    "novel view synthesis", "novel views from single image"
]

# 提取相关论文标题
titles = []
for paper in papers:
    text = (paper["title"] + " " + paper["abstract"]).lower()
    if any(keyword in text for keyword in keywords):
        titles.append(paper["title"])

# 打印标题到控制台
print(f"共找到 {len(titles)} 篇相关论文：\n")
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")

# 保存标题到 txt 文件
output_path = r"F:\single-view-3d\papers\3DV\2024\single_view_titles.txt"
with open(output_path, "w", encoding="utf-8") as f:
    for i, title in enumerate(titles, 1):
        f.write(f"{i}. {title}\n")

print(f"\n✅ 标题已保存到：{output_path}")
