# 📚 ICLR 2024 - Single-view 3D Reconstruction Paper List

## 📄 Paper List

---

### 1. LRM: Large Reconstruction Model for Single Image to 3D
**Authors**: Yicong Hong, Kai Zhang, Jiuxiang Gu, Sai Bi, Yang Zhou, Difan Liu, Feng Liu, Kalyan Sunkavalli, Trung Bui, Hao Tan  
**Affiliations**: Adobe Research, University of Maryland, ByteDance, Google Research

**Highlights**:
- 提出首个大规模单图 3D 重建模型（LRM），拥有 5 亿参数，采用 Transformer 架构。
- 模型可在 5 秒内从单张图像预测出神经辐射场（NeRF）。
- 在约 100 万个对象的多视图数据上进行端到端训练，包括 Objaverse 和 MVImgNet。
- 在真实世界图像和生成图像上表现出色，具备良好的泛化能力。

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2311.04400)

🔍 *Keywords*: Single-view 3D Reconstruction, Neural Radiance Fields, Large-scale Models  
🗂️ *Dataset*: Objaverse, MVImgNet

---

### 2. Generalizable Human Gaussians from Single-View Image
**Authors**: Jinnan Chen, Chen Li, Jianfeng Zhang, Lingting Zhu, Buzhen Huang, Hanlin Chen, Gim Hee Lee  
**Affiliations**: National University of Singapore, The University of Hong Kong

**Highlights**:
- 提出一种通用的人体高斯模型（HGM），可从单张图像中重建详细的人体外观和几何结构，包括不可见区域。
- 采用生成-精炼的流程，结合人体先验（SMPL-X）和扩散模型进行后视图精炼。
- 在多个公开数据集上验证了方法的有效性，表现优于现有方法。

## 🔗 Resources
[📄 Paper PDF](https://openreview.net/pdf/1bf3ed899eea2e5cf016fb537662bc271d0e552e.pdf)

🔍 *Keywords*: Single-view 3D Reconstruction, Human Modeling, Gaussian Splatting  
🗂️ *Dataset*: 多个公开人体数据集

---

### 3. GeoGS3D: Single-view 3D Reconstruction via Geometric-aware Gaussian Splatting
**Authors**: Qijun Feng, Zhen Xing, Zuxuan Wu, Yu-Gang Jiang  
**Affiliations**: Fudan University

**Highlights**:
- 提出 GeoGS3D，一种两阶段框架，从单张图像中重建详细的 3D 对象。
- 利用正交平面分解机制从 2D 输入中提取 3D 几何特征，生成多视图一致的图像。
- 引入新的度量指标 Gaussian Divergence Significance（GDS），加速优化过程。

## 🔗 Resources
[📄 Paper PDF](https://openreview.net/forum?id=I86z54CL2y)

🔍 *Keywords*: Single-view 3D Reconstruction, Diffusion Models, Gaussian Splatting  
🗂️ *Dataset*: 多个 3D 对象数据集

---

### 4. Template-Free Single-View 3D Human Digitalization with Diffusion-Guided LRM
**Authors**: Zhenzhen Weng, Jingyuan Liu, Hao Tan, Zhan Xu, Yang Zhou, Serena Yeung-Levy, Jimei Yang  
**Affiliations**: Stanford University, Adobe Research

**Highlights**:
- 提出 Human-LRM，一种无模板的单图 3D 人体数字化方法，结合 LRM 和扩散模型。
- 使用增强的几何解码器获取三平面 NeRF 表示，并通过扩散模型生成遮挡部分的细节。
- 在多个数据集上实现了高质量的几何和外观重建，优于现有人体重建方法。

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2401.12175)

🔍 *Keywords*: Single-view 3D Human Reconstruction, Diffusion Models, Neural Radiance Fields  
🗂️ *Dataset*: 多个人体数据集

---

### 5. 3D Reconstruction with Generalizable Neural Fields using Scene Priors
**Authors**: [作者信息待补充]  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 引入通用神经场（NFPs），将单视图 RGB-D 图像映射到符号距离和辐射值。
- 通过合并体积空间中的各个帧，无需融合模块即可重建完整场景。
- 支持单图像的新视角合成，在神经场中实现了未被充分探索的功能。

## 🔗 Resources
[📄 Paper PDF](https://iclr.cc/virtual/2024/poster/18765)

🔍 *Keywords*: Single-view 3D Reconstruction, Neural Fields, Scene Priors  
🗂️ *Dataset*: 大规模数据集

---

