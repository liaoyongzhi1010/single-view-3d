# 📚 ICLR 2025 - Single-view 3D Reconstruction Paper List

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
[📄 Paper PDF](https://arxiv.org/abs/2311.04400) | [🔗 Project Page](https://yiconghong.me/LRM)

🔍 *Keywords*: Single-view 3D Reconstruction, Neural Radiance Fields, Large-scale Models  
🗂️ *Dataset*: Objaverse, MVImgNet

---

### 2. GeoGS3D: Single-view 3D Reconstruction via Geometric-aware Diffusion Model and Gaussian Splatting
**Authors**: Qijun Feng, Zhen Xing, Zuxuan Wu, Yu-Gang Jiang  
**Affiliations**: Fudan University

**Highlights**:
- 提出 GeoGS3D，一种两阶段框架，从单张图像中重建详细的 3D 对象。
- 利用正交平面分解机制从 2D 输入中提取 3D 几何特征，生成多视图一致的图像。
- 引入新的度量指标 Gaussian Divergence Significance（GDS），加速优化过程。

## 🔗 Resources
[📄 Paper PDF](https://openreview.net/pdf/dd44ed0f0cb67e3ffe5a3eb9ad550cd5272adc4d.pdf) | [🔗 Project Page](https://geogs3d.github.io)

🔍 *Keywords*: Single-view 3D Reconstruction, Diffusion Models, Gaussian Splatting  
🗂️ *Dataset*: 多个 3D 对象数据集

---

### 3. Generalizable Human Gaussians from Single-View Image
**Authors**: Jinnan Chen, Chen Li, Jianfeng Zhang, Lingting Zhu, Buzhen Huang, Hanlin Chen, Gim Hee Lee  
**Affiliations**: National University of Singapore, The University of Hong Kong

**Highlights**:
- 提出一种通用的人体高斯模型（HGM），可从单张图像中重建详细的人体外观和几何结构，包括不可见区域。
- 采用生成-精炼的流程，结合人体先验（SMPL-X）和扩散模型进行后视图精炼。
- 在多个公开数据集上验证了方法的有效性，表现优于现有方法。

## 🔗 Resources
[📄 Paper PDF](https://openreview.net/pdf/1bf3ed899eea2e5cf016fb537662bc271d0e552e.pdf) | [💻 Code Repository](https://github.com/jinnan-chen/HGM)

🔍 *Keywords*: Single-view 3D Reconstruction, Human Modeling, Gaussian Splatting  
🗂️ *Dataset*: 多个公开人体数据集

---

### 4. ACT-R: Adaptive Camera Trajectories for 3D Reconstruction from Single Image
**Authors**: Yizhi Wang, Mingrui Zhao, Ali Mahdavi-Amiri, Hao Zhang  
**Affiliations**: Simon Fraser University

**Highlights**:
- 引入自适应视角规划到多视图合成，以提高遮挡区域的揭示和 3D 一致性。
- 生成一系列视角，利用时间一致性增强 3D 连贯性。
- 在多个数据集上实现了高质量的重建效果。

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2505.08239)

🔍 *Keywords*: Single-view 3D Reconstruction, Adaptive View Planning, Diffusion Models  
🗂️ *Dataset*: GSO 等

---

### 5. NeuralPlane: Structured 3D Reconstruction in Planar Primitives with Neural Fields
**Authors**: Hanqiao Ye, Yuzhou Liu, Yangdong Liu, Shuhan Shen  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 提出 NeuralPlane，一种基于神经场的多视图 3D 平面重建方法。
- 通过从不一致的 2D 平面观察中提取几何和语义线索，构建统一的 3D 神经表示。
- 在 ScanNetv2 和 ScanNet++ 上进行了全面实验，展示了方法在几何和语义方面的优越性。

## 🔗 Resources
[📄 Paper PDF](https://iclr.cc/virtual/2025/events/oral)

🔍 *Keywords*: Single-view 3D Reconstruction, Neural Fields, Planar Primitives  
🗂️ *Dataset*: ScanNetv2, ScanNet++

---

