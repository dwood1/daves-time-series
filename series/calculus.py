# Difference
def difference(input_array, interval=1, order=1, keep_interval=False):
    l = len(input_array)
    output_array = [0] * len(input_array)
    new_interval =  interval if keep_interval else 1
    temp_array = difference(input_array, new_interval, order-1, keep_interval) if order > 1 else input_array
    for t in range(interval, l):
        output_array[t] = temp_array[t] - temp_array[t-interval]

    return output_array