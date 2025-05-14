# 📚 CVPR 2024 - Single-view 3D Reconstruction Paper List

## 📄 Paper List

---

### 1. Splatter Image: Ultra-Fast Single-View 3D Reconstruction
**Authors**: Stanislaw Szymanowicz, Christian Rupprecht, Andrea Vedaldi  
**Affiliations**: University of Oxford

**Highlights**:
- 提出了一种基于高斯散点的单图三维重建方法。
- 输入图像经神经网络映射为每像素 3D 高斯分布，实时重建速度高达 38 FPS。
- 高效、端到端，重建质量与速度远超现有方法。

## 🔗 Resources
[📄 Paper PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Szymanowicz_Splatter_Image_Ultra-Fast_Single-View_3D_Reconstruction_CVPR_2024_paper.pdf) | [🔗 Project Page](https://szymanowiczs.github.io/splatter-image) | [💻 Code Repository](https://github.com/szymanowiczs/splatter-image)

🔍 *Keywords*: Single-view 3D Reconstruction, Gaussian Splatting, Real-time Rendering  
🗂️ *Dataset*: Synthetic and real multi-category datasets

---

### 2. Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers
**Authors**: Zi-Xin Zou, Zhipeng Yu, Yuan-Chen Guo, Yangguang Li, Ding Liang, Yan-Pei Cao, Song-Hai Zhang  
**Affiliations**: Tsinghua University, SenseTime Research

**Highlights**:
- 结合 Triplane 表示与高斯散点，使用 Transformer 构建单图 3D 重建模型。
- 泛化能力强，在多数据集上保持一致高性能。

## 🔗 Resources
[📄 Paper PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.pdf)

🔍 *Keywords*: Single-view 3D Reconstruction, Triplane Representation, Gaussian Splatting, Transformers  
🗂️ *Dataset*: Various benchmark datasets

---

### 3. SiTH: Single-view Textured Human Reconstruction with Image-Conditioned Diffusion
**Authors**: Hsuan-I Ho, Jie Song, Otmar Hilliges  
**Affiliations**: ETH Zurich

**Highlights**:
- 利用图像条件扩散模型，实现纹理化人体的单图重建。
- 生成完整 3D 人体仅需 2 分钟，结合条件控制与纹理生成。

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2404.12345) | [💻 Code Repository](https://github.com/SiTH-Diffusion/SiTH)

🔍 *Keywords*: Single-view 3D Reconstruction, Human Reconstruction, Diffusion Models  
🗂️ *Dataset*: Human3.6M, SURREAL

---

### 4. Slice3D: Multi-Slice Occlusion-Revealing Single View 3D Reconstruction
**Authors**: Yizhi Wang, Wallace Lira, Wenqi Wang, Ali Mahdavi-Amiri, Hao Zhang  
**Affiliations**: Simon Fraser University

**Highlights**:
- 多切片重建方法能有效揭示遮挡区域，提高遮挡场景下的重建完整性。
- 切片结构能平衡精细建模与效率，提升遮挡理解能力。

## 🔗 Resources
[📄 Paper PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_Slice3D_Multi-Slice_Occlusion-Revealing_Single_View_3D_Reconstruction_CVPR_2024_paper.pdf)

🔍 *Keywords*: Single-view 3D Reconstruction, Occlusion Handling, Multi-Slice Representation  
🗂️ *Dataset*: ShapeNet, Pix3D

---

### 5. Gamba: Marry Gaussian Splatting with Mamba for Single View 3D Reconstruction
**Authors**: Qiuhong Shen, Zike Wu, Xuanyu Yi, Pan Zhou, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  
**Affiliations**: National University of Singapore

**Highlights**:
- 将 Gaussian Splatting 与 Mamba 架构结合，实现超快单图 3D 重建。
- 推理时间仅需 0.05 秒，比优化方法快 1000 倍。

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2403.18795) | [🔗 Project Page](https://florinshen.github.io/gamba-project)

🔍 *Keywords*: Single-view 3D Reconstruction, Gaussian Splatting, Mamba Architecture  
🗂️ *Dataset*: Objaverse, GSO

---
