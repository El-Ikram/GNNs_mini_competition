# GNNs Mini Competition: Chest X-ray Graph Classification
<p align="center">
Not all graphs are social networks, some can help diagnose lungs.
 
Behind every chest X-ray lies a complex story waiting to be understood.

Welcome to this GNN mini-challenge!! Where chest X-rays become graphs and your model decides: Normal or Pneumonia.
</p>

 ## 💢Problem Description 
 A chest X-ray is a medical imaging technique that uses a small amount of radiation to create images of the structures inside the chest, including the lungs, heart, and airways. It is one of the most common and important tools used by doctors to examine lung conditions.

Chest X-ray images are classified into two categories:

Normal:
The lungs appear healthy, with no visible signs of infection, inflammation, or abnormal fluid. The lung fields are clear and show normal structure.

Pneumonia:
Pneumonia is a lung infection that causes inflammation of the air sacs in one or both lungs. On a chest X-ray, pneumonia often appears as opaque or cloudy regions, indicating the presence of fluid or infection in the lungs.

Accurate classification of chest X-ray images can help support early detection of pneumonia and improve patient care. \
In this mini-challenge, The goal of this challenge is to perform graph classification on chest X-ray images.

Each chest X-ray image is converted into a graph, where:

* Nodes represent image regions or patches.
* Edges represent spatial or similarity-based relationships.
* Node features are extracted from image intensities or handcrafted features.
* Each graph corresponds to one patient image and has a single label:\
0 → Normal\
1 → Pneumonia

Participants will design Graph Neural Network (GNN) models that leverage both node features and the graph structure to classify each X-ray image correctly.

 ## 🛢️Dataset
This mini-challenge uses the Chest X-Ray Images (Pneumonia) dataset, a widely used public medical imaging dataset for lung disease classification. The dataset contains frontal chest X-ray images collected from pediatric patients and labeled by medical experts as either Normal or Pneumonia.\
The dataset is class-imbalanced, with more Pneumonia images than Normal images. Participants should take this imbalance into account during training and evaluation:
* Training set -> Normal = 1341 | Pneunomia = 3875
* Test set -> Normal = 234 | Pneumonia = 390
* Total -> Normal = 1575 | Pneumonia = 4265

Below are example chest X-ray images from the dataset, illustrating the visual differences between Normal and Pneumonia cases.\
<p align="center">
  <img src="Images/NORMAL2-IM-1427-0001.jpeg" height="230"  />
  <img src="Images/person1949_bacteria_4880.jpeg" height="230"  />
</p>

<p align="center">
  <em>Left: Normal chest X-ray | Right: Pneumonia chest X-ray</em>
</p>
The dataset is publicly available on Kaggle.

🔗 **Dataset link:**  [Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

🔗**Related publication:**  Kermany, D. S., Goldbaum, M., Cai, W., et al. (2018). *[Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning](https://www.sciencedirect.com/science/article/pii/S0092867418301545)*.  

Files available in data/

- **Train set:** Images with ground-truth labels (Normal / Pneumonia).
- **Test set:** Images without labels. Participants must submit predictions for these images.


# <img width="45" height="45" alt="image" src="https://github.com/user-attachments/assets/6e05cfef-3064-4d6d-bf4b-ea9259f21e11" />Evaluation metric
Model performance will be assessed using the **Macro F1-score**, which is well-suited for imbalanced classification tasks such as this one.

The Macro F1-score is calculated by:
1. Computing the F1-score separately for each class.
2. Taking the unweighted average of these class-level F1-scores.

By giving equal importance to each class regardless of its frequency, the Macro F1-score ensures that performance on minority classes (such as less common labels) is not overlooked.

Higher Macro F1 values indicate better overall classification quality across all classes.

## ⚠️Constraints
To ensure fair competition:
1. No External Data, only the data provided for this challenge may be used.
2. No external node features, it must be derived solely from the given dataset.
3. No pretrained embeddings or models, all models must be trained from scratch using the provided data.
4. Maximum of 2 GNN layers, keep your model simple and interpretable (deeper is not always better).
   
Think of this as a “from-scratch GNN challenge”, no shortcuts, no pretrained magic, just pure graph learning✨


## 📤Submission
Ready to compete? Follow these steps to get your model on the leaderboard 
* Each participant needs to fork this repository to his GitHub account.
* Each participant needs to use the provided starter code as a baseline and implement your GNN model (while respecting all constraints!).
* Each participant after generating predictions for the test set needs to save them as a CSV file with the required format:\
   Participant , Score .
* Score the submissions.
* Create a Pull Request.
* After evaluating the submission, the score will appear on the leaderboard.

 🌟Higher scores climb higher🌟
  
## 🏆Leaderboard
The competition features a **dynamic, automatically updated leaderboard**.
* All scores are stored and displayed in real-time on leaderboard/index.html.
* Participants are ranked according to the official evaluation metric (Macro F1-score).
* Each entry shows: Rank, Team Name, Score, and Submission Date.
* The leaderboard updates automatically whenever a valid submission is made via a Pull Request, no manual intervention is needed.

✨Watch your team climb the ranks as you submit! 

[View the live leaderboard](https://El-Ikram.github.io/CXR_Normal_vs_Pneumonia_Node_Classification/leaderboard/index.html)

## 📚References
* Basira's lab lectures on GNNs: [DGL_Videos](https://www.youtube.com/watch?v=gQRV_jUyaDw&list=PLug43ldmRSo14Y_vt7S6vanPGh-JpHR7T).
* Dataset: [Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia).

## 📄License
This project is released under the **MIT License**.  
You are free to use, modify, and distribute the code for research and educational purposes, with proper attribution.\
The Chest X-Ray Images (Pneumonia) dataset is provided by Kaggle and is subject to its original license and usage terms.

See the [LICENSE](LICENSE) file for details.
