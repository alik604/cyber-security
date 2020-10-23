# warning 

in some pytorch files `y_test_vals = y_test.values` needs to be `y_test_vals = y_test.values.flatten()` 

thankfuly this causes a breaking error. However, I just wasted 10mins debugging beecause I only fixed this in the train loop, and not in the test. 
