# 📚 ICML 2025 - Single-view 3D Reconstruction Paper List

## 📄 Paper List

---

### 1. Flex3D: Feed-Forward 3D Generation With Flexible Reconstruction Model and Input View Curation
**Authors**: Junlin Han, Jianyuan Wang, Andrea Vedaldi, Philip Torr, Filippos Kokkinos  
**Affiliations**: GenAI (Meta), University of Oxford

**Highlights**:
- 提出 Flex3D，一种两阶段框架，支持从单张图像或文本提示生成高质量的 3D 内容。
- 第一阶段生成多视图候选图像，并通过质量和一致性筛选机制进行筛选。
- 第二阶段使用基于 Transformer 的 Flexible Reconstruction Model（FlexRM）处理任意数量的输入视图，直接输出 3D 高斯点云。
- 在 3D 生成任务中，用户研究显示 Flex3D 的胜率超过 92%，优于多种最新的前馈 3D 生成模型。

## 🔗 Resources
[📄 Paper PDF](https://openreview.net/forum?id=2vaTZH31oR) | [🔗 Project Page](https://junlinhan.github.io/projects/flex3d/)

🔍 *Keywords*: Single-view 3D Reconstruction, Feed-Forward Networks, Gaussian Splatting, Transformer  
🗂️ *Dataset*: Synthetic and real multi-category datasets

---

### 2. Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View
**Authors**: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 提出 Niagara，一种用于单图三维场景重建的新框架，特别适用于高保真户外场景建模。
- 结合单目深度和法线估计作为输入，显著提高了对细节的捕捉能力，缓解了几何细节丢失和变形等常见问题。
- 引入几何仿射场（GAF）和 3D 自注意力机制，结合显式几何结构和隐式特征场的结构属性，实现高效渲染和高保真重建的平衡。
- 实验结果表明，Niagara 在单视图和双视图设置中均优于现有方法，如 Flash3D，显著提升了几何精度和视觉保真度，特别是在户外场景中。

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2503.12553)

🔍 *Keywords*: Single-view 3D Reconstruction, Outdoor Scenes, Geometric Affine Field, Gaussian Splatting  
🗂️ *Dataset*: Outdoor scene datasets

---

*请注意：由于目前 ICML 2025 的完整论文列表尚未公开，以上仅为部分已知的代表性论文。建议您定期访问 [ICML 2025 官方网站](https://icml.cc/) 以获取最新的论文信息和资源。*
