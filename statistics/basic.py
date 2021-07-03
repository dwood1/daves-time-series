# AVERAGE
def average(input_array):
    # time: O(n), space: O(1)
    return sum(input_array) / len(input_array)


def sample_average(input_array):
    # time: O(n), space: O(1)
    return sum(input_array) / (len(input_array)-1)

# VARIANCE


def variance(input_array):
    # time: O(n), space: O(n)
    x_bar = average(input_array)
    return average([(x-x_bar)**2 for x in input_array])


def sample_variance(input_array):
    # time: O(n), space: O(n)
    n = len(input_array)
    sAvg = sample_average(input_array)
    return sample_average([(input_array[i] - sAvg)**2
                           for i in range(n)])

# STANDARD DEVIATION


def standard_deviation(input_array):
    # time: O(n), space: O(n)
    avg = average(input_array)
    return average([(avg - i) for i in input_array])


def sample_standard_deviation(input_array):
    # time: O(n), space: O(n)
    n = len(input_array)
    sAvg = sample_average(input_array)
    return (sample_average([(input_array[i] - sAvg)**2
                            for i in range(n)]))**(0.5)

# COVARIANCE


def covariance(x_array, y_array=[]):
    # time: O(n), space: O(n)
    l_x = len(x_array)
    x_bar = average(x_array)
    if(y_array == []):
        y_bar = (l_x-1)/2
        xy_bar = average([x_array[i]*i for i in range(l_x)])
        return (xy_bar - (x_bar*y_bar))
    elif(l_x != len(y_array)):
        print("The arrays must be the same length!")
        return []
    else:
        loop_xy = zip(x_array, y_array)
        y_bar = average(y_array)
        xy_bar = average([x*y for x, y in loop_xy])
        return (xy_bar - (x_bar*y_bar))
