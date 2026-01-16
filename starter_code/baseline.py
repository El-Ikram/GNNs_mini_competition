import pandas as pd
2 from sklearn . model_selection import train_test_split
3 from sklearn . ensemble import RandomForestClassifier
4 from sklearn . metrics import f1_score
5
6 # Load data
7 train = pd . read_csv ('../ data / train .csv ')
8 X = train . drop ('target ', axis =1)
9 y = train ['target ']
10
11 # Split into train / validation
12 X_train , X_val , y_train , y_val = train_test_split (X , y , test_size =0.2 , random_state
=42)
13
14 # Train a baseline model
15 clf = RandomForestClassifier ( n_estimators =100 , random_state =42)
16 clf . fit ( X_train , y_train )
17
18 # Evaluate
19 y_pred = clf . predict ( X_val )
20 score = f1_score ( y_val , y_pred , average ='macro ')
21 print ( f'Validation F1 Score : { score :.4f}')
22
23 # Make predictions on test set
24 test = pd . read_csv ('../ data / test .csv ')
25 test_preds = clf . predict ( test )
26 pd . DataFrame ({ 'id ': test ['id '] , 'target ': test_preds }) . to_csv ('../ submissions /
sample_submission . csv ', index = False )
