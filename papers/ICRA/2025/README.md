# 📚 ICRA 2025 - Single-view 3D Reconstruction Paper List

## 📄 Paper List

---

### 1. Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View
**Authors**: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser‑Nam Lim, Jun Liu, Huan Wang  
**Affiliations**: (详见论文)

**Highlights**:
- 针对室外场景提出了 Niagara，将单目深度 + 法线估计作为输入，显著提升几何细节捕捉能力。
- 引入几何仿射场（GAF）与 3D 自注意力，结合显式与隐式特征，平衡高保真与高效渲染。
- 设计深度驱动的 3D Gaussian 解码器，可用于新视点合成。
- 在 Flash3D 等方法基础上，在单视图/双视图设置中几何精度和视觉保真度上均有明显提升。 :contentReference[oaicite:0]{index=0}

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2503.12553)

🔍 *Keywords*: Single-view 3D Reconstruction, Geometric Affine Field, Gaussian Splatting  
🗂️ *Dataset*: 室外场景数据集

---

### 2. ACT‑R: Adaptive Camera Trajectories for 3D Reconstruction from Single Image
**Authors**: Yizhi Wang, Mingrui Zhao, Ali Mahdavi‑Amiri, Hao Zhang  
**Affiliations**: (详见论文)

**Highlights**:
- 提出自适应相机轨迹（ACT）策略，在合成多视图时动态规划一条“最佳”轨迹以揭示遮挡区域。
- 轨迹生成后，利用视频扩散模型合成该轨迹下的新视图，再交给多视图重建模型，整个流程无需在线优化。
- 在 GSO 数据集上显著提升了对遮挡区域的重建效果和整体一致性。 :contentReference[oaicite:1]{index=1}

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2505.08239)

🔍 *Keywords*: Single-view 3D Reconstruction, Adaptive View Planning, Diffusion‑based Novel View Synthesis  
🗂️ *Dataset*: Google Scanned Objects (GSO)

---

### 3. CHROME: Clothed Human Reconstruction with Occlusion‑Resilience and Multiview‑Consistency from a Single Image
**Authors**: Arindam Dutta, Meng Zheng, Zhongpai Gao, Benjamin Planche, Anwesha Choudhuri, Terrence Chen, Amit K. Roy‑Chowdhury, Ziyan Wu  
**Affiliations**: (详见论文)

**Highlights**:
- 针对有遮挡的单张人体图像，先用多视图扩散模型合成无遮挡人像，再基于合成视图和原图预测一组 3D Gaussians。
- 无需 SMPL 等几何先验标签或 3D 监督，即可生成多视图一致且对遮挡鲁棒的 3D 人体模型。 :contentReference[oaicite:2]{index=2}

## 🔗 Resources
[📄 Paper PDF](https://arxiv.org/abs/2503.15671)

🔍 *Keywords*: Single-view Human Reconstruction, Occlusion‑Resilience, Gaussian Splatting  
🗂️ *Dataset*: 多视图人体数据

---

*注：以上为目前公开的几篇代表性工作。如需进一步补充其他子方向（如工业部件、室内场景或基于深度传感器的方法），请告诉我！*  
