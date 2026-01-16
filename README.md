# GNNs_mini_competition
# Predict the research area of a paper based on citation links

 # Problem Description
 Given a citation graph where nodes represent scientific papers and edges represent citations, predict the research field of each paper using graph neural networks.

 # Dataset
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

# Leaderboard

# References
Basira's lab lectures on GNNs.
