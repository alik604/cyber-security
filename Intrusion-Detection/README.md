# Note  

1. in some pytorch files `y_test_vals = y_test.values` needs to be `y_test_vals = y_test.values.flatten()` 

> thankfully this causes a breaking error. However, I just wasted 10mins debugging because I only fixed this in the train loop, and not in the test loop [of a neural net made in pytorch]. 
