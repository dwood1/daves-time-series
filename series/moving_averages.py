from statistics import statistics as st
#Moving Average
def moving_average(input_array, interval):
    # time: O(n), space: O(n)
    
    output_array = [x for x in input_array]
    output_array[interval-1] = st.average(input_array[:interval])
    
    for t in range(interval, len(input_array)):
        output_array[t] = output_array[t-1] + ((input_array[t] - input_array[t-interval]) / interval)
       
    return output_array

#Exponential Moving Average
def exponential_moving_average(input_array, interval, smoothing=2):
    output_array = [*input_array]
    output_array[interval-1] = st.average(input_array[:interval])
    factor = (smoothing/(1+interval))    
    for t in range(interval, len(input_array)):        
        output_array[t] = output_array[t-1]*(1-factor) + input_array[t]*factor
       
    return output_array

#Linear Moving Average
def linear_moving_average(input_array, interval):
    output_array = [*input_array]
    weight_factor = interval*(interval+1)/2
    avg_interval = input_array[:interval]
    output_array[interval-1] = sum([avg_interval[i]*(interval-i) for i in range(interval)])/weight_factor
    for t in range(interval, len(input_array)):
        avg_interval.pop(0)
        avg_interval.append(input_array[t])
        output_array[t] = sum([avg_interval[i]*(interval-i) for i in range(interval)])/weight_factor
        
    return output_array

#Hull Moving Average
def hull_moving_average(input_array, interval):
    wma = linear_moving_average(input_array, int(interval/2))
    wma_2 = linear_moving_average(input_array, interval)
    wma_diff = [2*wma[t] - wma_2[t] for t in range(len(wma))] 
    wma_3 = linear_moving_average(wma_diff, int(interval**(0.5)))
    return wma_3