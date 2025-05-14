# 📚 ECCV 2024 - Single-view 3D Reconstruction Paper List

## 📄 Paper List

---

### 1. Analysis-by-Synthesis Transformer for Single-View 3D Reconstruction
**Authors**: Dian Jia, Xiaoqian Ruan, Kun Xia, Zhiming Zou, Le Wang, Wei Tang  
**Affiliations**: University of Science and Technology of China, University of Illinois at Chicago

**Highlights**:
- 提出了一种统一的分析-合成 Transformer 框架，结合 Shape Transformer 和 Texture Transformer。
- Shape Transformer 使用可学习的形状查询，从图像中提取像素级特征，实现高质量网格重建并恢复遮挡顶点。
- Texture Transformer 利用纹理查询进行非局部纹理信息聚合，消除不正确的归纳偏差。
- 在 CUB-200-2011 和 ShapeNet 数据集上，在形状重建和纹理生成方面表现优于现有方法。

## 🔗 Resources
[📄 Paper PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03170.pdf) | [🔗 Project Page](https://www.evl.uic.edu/pubs/2866) | [💻 Code Repository](https://github.com/DianJJ/AST)

🔍 *Keywords*: Single-view 3D Reconstruction, Analysis-by-Synthesis, Transformer, Shape Transformer, Texture Transformer  
🗂️ *Dataset*: CUB-200-2011, ShapeNet

---

### 2. GSD: View-Guided Gaussian Splatting Diffusion for 3D Reconstruction
**Authors**: [作者信息待补充]  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 提出了一种基于高斯散点表示的扩散模型，用于从单视图图像进行 3D 对象重建。
- 模型学习生成由高斯椭球体组成的 3D 对象集合，具有强大的生成能力。
- 通过传播细粒度的 2D 特征和引导去噪采样过程，实现了无需进一步微调的视图引导重建。

## 🔗 Resources
[📄 Paper PDF](https://eccv.ecva.net/virtual/2024/poster/1307) | [🔗 Project Page](https://eccv.ecva.net/virtual/2024/poster/1307) | [💻 Code Repository](链接待补充)

🔍 *Keywords*: Single-view 3D Reconstruction, Gaussian Splatting, Diffusion Model, View-Guided Reconstruction  
🗂️ *Dataset*: [数据集信息待补充]

---

### 3. SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion
**Authors**: Vikram Voleti, Chun-Han Yao, Mark Boss, Adam Letts, David Pankratz, Dmitrii Tochilkin, Christian Laforte, Robin Rombach, Varun Jampani  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 提出了一种名为 Stable Video 3D (SV3D) 的潜在视频扩散模型，用于从单张图像生成高分辨率的多视图合成和 3D 生成。
- 模型利用视频扩散模型的泛化能力和多视图一致性，增强了新视图合成的质量。
- 引入了改进的 3D 优化技术，利用 SV3D 及其新视图合成输出进行图像到 3D 的生成。

## 🔗 Resources
[📄 Paper PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00150.pdf) | [🔗 Project Page](链接待补充) | [💻 Code Repository](链接待补充)

🔍 *Keywords*: Single-view 3D Reconstruction, Multi-view Synthesis, Latent Video Diffusion, Novel View Synthesis  
🗂️ *Dataset*: [数据集信息待补充]

---

### 4. GeoGS3D: Single-view 3D Reconstruction via Geometric-aware Gaussian Splatting
**Authors**: [作者信息待补充]  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 提出了一种名为 GeoGS3D 的两阶段框架，从单视图图像重建详细的 3D 对象。
- 采用正交平面分解机制，从 2D 输入中提取 3D 几何特征，促进多视图一致图像的生成。
- 在后续的高斯散点过程中，这些图像通过极线注意力进行融合，充分利用跨视图的几何相关性。

## 🔗 Resources
[📄 Paper PDF](链接待补充) | [🔗 Project Page](https://geogs3d.github.io/) | [💻 Code Repository](链接待补充)

🔍 *Keywords*: Single-view 3D Reconstruction, Geometric-aware, Gaussian Splatting, Multi-view Consistency  
🗂️ *Dataset*: [数据集信息待补充]

---

### 5. Part123: Part-aware 3D Reconstruction from a Single-view Image
**Authors**: [作者信息待补充]  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 提出了一种名为 Part123 的新颖框架，用于从单视图图像进行部件感知的 3D 重建。
- 首先使用扩散模型生成部件的 3D 表示，然后将这些部件组合成完整的 3D 对象。
- 方法在多个数据集上展示了优越的性能，尤其在处理复杂结构的对象时表现出色。

## 🔗 Resources
[📄 Paper PDF](https://dl.acm.org/doi/10.1145/3641519.3657482) | [🔗 Project Page](链接待补充) | [💻 Code Repository](链接待补充)

🔍 *Keywords*: Single-view 3D Reconstruction, Part-aware, Diffusion Model, 3D Object Composition  
🗂️ *Dataset*: [数据集信息待补充]

---

