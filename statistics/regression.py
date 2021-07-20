from statistics import statistics as st

# linear regression
def linear_regression_channel(input_array, interval, deviations=1): 
    # time: O(n*i), space: O(n*i)   
    output_array = [(x, x, x) for x in input_array]
        
    for t in range(interval-1, len(input_array)):
        x = [i for i in range(t-interval+1,t+1)]
        y = input_array[t-interval+1:t+1]
        x_bar = st.average(x)
        y_bar = st.average(y)
        cov = st.covariance(x, y)
        var_x = st.variance(x)
        stdev_y = (st.variance(y)**0.5)*deviations
        m = cov/var_x
        b = y_bar - (m*x_bar)
        reg_val = m*t+b
        # print(stdev_y, cov, var_x, m, b, x_bar, y_bar, m*t+b)
        output_array[t] = (reg_val-stdev_y, reg_val, reg_val+stdev_y)
    
    return output_array