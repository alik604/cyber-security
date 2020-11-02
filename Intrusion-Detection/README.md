# Note  

1. in some pytorch files `y_test_vals = y_test.values` needs to be `y_test_vals = y_test.values.flatten()` 

> thankfully this causes a breaking error. However, I just wasted 10mins debugging beecause I only fixed this in the train loop, and not in the test. 


2. in UNSW_NB15 Unsupervised, the following line is completly incorrect
`print(f'Acc of train: {100*np.sum(y_train.iloc[idx]).values[0]/y_train.iloc[idx].shape[0]:.4f} with votes: {VOTES}')` 
> Not sure what I was thinking. its not a quick fix... 
