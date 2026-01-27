# GNNs Mini Competition: Chest X-ray Normal vs Pneumonia (Node Classification)
 # 💢Problem Description 
 A chest X-ray is a medical imaging technique that uses a small amount of radiation to create images of the structures inside the chest, including the lungs, heart, and airways. It is one of the most common and important tools used by doctors to examine lung conditions.

Chest X-ray images are classified into two categories:

Normal:
The lungs appear healthy, with no visible signs of infection, inflammation, or abnormal fluid. The lung fields are clear and show normal structure.

Pneumonia:
Pneumonia is a lung infection that causes inflammation of the air sacs in one or both lungs. On a chest X-ray, pneumonia often appears as opaque or cloudy regions, indicating the presence of fluid or infection in the lungs.

Accurate classification of chest X-ray images can help support early detection of pneumonia and improve patient care. \
In this mini-challenge, the goal is to classify chest X-ray images as Normal or Pneumonia using graph-based learning.



 # 🛢️Dataset
We use the Cora citation network, where:\
Nodes = papers\
Edges = citations\
Labels = research topics\

# Evaluation metric
We evaluate performance using Macro F1-score, which is suitable for imbalanced node classification tasks.\
The Macro F1-score is computed by first calculating the F1-score independently for each class and then averaging these scores, assigning equal weight to all classes regardless of their frequency.

# Constraints
To ensure fair competition:\
1.No External Data.\
2.No external node features.\
3.No pretrained embeddings.\
4.Maximum of 2 GNN layers.

# Submission
* Each participant needs to fork this repository to his GitHub account.
* Each participant needs build his model using the starter code.
* Each participant after generating predictions for the test set needs to save them as a CSV file with the required format:\
  Participant : Score.
* Score the submissions.
* Create a Pull Request.
* After evaluating the submission, the score will appear on the leaderboard.
  
# Leaderboard
All evaluation results will be published in the file Leaderboard.md.\
Participants will be ranked according to the official evaluation metric.\
Each entry will include the participant name, score, and submission date.\
The leaderboard will be updated after each valid submission.
# References
Basira's lab lectures on GNNs.
