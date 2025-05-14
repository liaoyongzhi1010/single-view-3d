# 📚 NeurIPS 2024 - Single-view 3D Reconstruction Paper List

## 📄 Paper List

---

### 1. Hamba: Single-view 3D Hand Reconstruction with Graph-guided Bi-Scanning Mamba
**Authors**: Haoye Dong, Aviral Chharia, Wenbo Gou, Francisco Vicente Carrasco, Fernando De la Torre  
**Affiliations**: Carnegie Mellon University

**Highlights**:
- 提出了一种结合图引导状态空间模型的 Mamba 架构，用于高效建模手部关节之间的空间关系。
- 设计了 Graph-guided State Space (GSS) 模块，使用比基于注意力的方法少 88.5% 的 token。
- 在 FreiHAND 数据集上实现了 PA-MPVPE 5.3mm 和 F@15mm 0.992 的性能，位列两个 3D 手部重建排行榜第一。:contentReference[oaicite:21]{index=21}

## 🔗 Resources
[📄 Paper PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/03e9a69e5b686c316a07d73f0cf5e225-Paper-Conference.pdf) | [🔗 OpenReview](https://openreview.net/forum?id=pCJ0l1JVUX) | [🎥 Presentation Video](https://www.youtube.com/watch?v=HKGU64myW94)

🔍 *Keywords*: Single-view 3D Hand Reconstruction, Graph-guided Mamba, State Space Model  
🗂️ *Dataset*: FreiHAND

---

### 2. Geometry Cloak: Preventing TGS-based 3D Reconstruction from Copyrighted Images
**Authors**: Qi Song, Ziyuan Luo, Ka Chun Cheung, Simon See, Renjie Wan  
**Affiliations**: [机构信息待补充]

**Highlights**:
- :contentReference[oaicite:23]{index=23}
- :contentReference[oaicite:26]{index=26}:contentReference[oaicite:28]{index=28}

## 🔗 Resources
[📄 Paper Abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d7e7ab160ebcece4f80d1315f957a5ce-Abstract-Conference.html)

🔍 *Keywords*: Single-view 3D Reconstruction, Triplane Gaussian Splatting, Image Protection  
🗂️ *Dataset*: [数据集信息待补充]

---

### 3. Physically Compatible 3D Object Modeling from a Single Image
**Authors**: Minghao Guo, Bohan Wang, Pingchuan Ma, Tianyuan Zhang, Crystal Elaine Owens, Chuang Gan, Joshua B. Tenenbaum, Kaiming He, Wojciech Matusik  
**Affiliations**: IBM Research, MIT, Meta AI

**Highlights**:
- 提出了一种计算框架，将单张图像转换为具有物理兼容性的 3D 物体模型。
- 通过显式分解物体的机械属性、外部力和静止形状几何，并通过静力平衡将其联系起来，确保优化后的物理形状表现出期望的物理行为。:contentReference[oaicite:33]{index=33}

## 🔗 Resources
[📄 Paper Abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d7af02c8a8e26608199c087f50a21d37-Abstract-Conference.html)

🔍 *Keywords*: Single-view 3D Reconstruction, Physical Compatibility, Static Equilibrium  
🗂️ *Dataset*: Objaverse

---

### 4. L4GM: Large 4D Gaussian Reconstruction Model
**Authors**: Jiawei Ren, Cheng Xie, Ashkan Mirzaei, Hanxue Liang, Xiaohui Zeng, Karsten Kreis, Ziwei Liu, Antonio Torralba, Sanja Fidler, Seung Wook Kim, Huan Ling  
**Affiliations**: [机构信息待补充]

**Highlights**:
- 提出了 L4GM，第一个从单视图视频输入生成动画对象的 4D 大型重建模型。
- 该模型在一次前馈传递中生成每帧的 3D 高斯点云表示，并通过插值模型将其上采样到更高的帧率，实现时间上的平滑性。:contentReference[oaicite:38]{index=38}

## 🔗 Resources
[📄 Paper PDF](https://papers.nips.cc/paper_files/paper/2024/file/6808f2c57d9564a2639a4710e3bbd9b9-Paper-Conference.pdf)

🔍 *Keywords*: Single-view 3D Reconstruction, 4D Gaussian Splatting, Dynamic Objects  
🗂️ *Dataset*: Objaverse

---

*请注意：由于目前 NeurIPS 2025 的完整论文列表尚未公开，以上为 NeurIPS 2024 中的代表性论文。建议您定期访问 [NeurIPS 2025 官方网站](https://neurips.cc/) 以获取最新的论文信息和资源。*
