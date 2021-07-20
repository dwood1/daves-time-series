from statistics import statistics as st
from series import calculus as ca
from utilities import utilities as utils


#Stochastic
def stochastic(input_array, interval, scale=False):
    output_array = [50]*len(input_array) if scale else [0.5]*len(input_array)
    stochastic_interval = []
    for t in range(interval-1, len(input_array)):
        stochastic_interval = input_array[t-interval+1:t+1]
        max_val = max(stochastic_interval)
        min_val = min(stochastic_interval)
        new_val = (input_array[t] - min_val) / (max_val - min_val) if max_val != min_val else 1
        output_array[t] = new_val*100 if scale else new_val
    return output_array

#RSI
def rsi(input_array, interval=14, scale=True, agg_type="AVG"):
    agg_func = {"AVG":lambda x : st.average(x), "SUM": lambda x : sum(x), "MAX": lambda x : max(x), "MIN": lambda x : min(x)}
    output_array = [50]*len(input_array) if scale else [0]*len(input_array)
    
    dxr = ca.difference(input_array, 1, 1)
    
    avg_gain = [x for x in dxr[:interval] if x >= 0]
    avg_loss = [x for x in dxr[:interval] if x < 0]
    
    avg_gain = agg_func[agg_type](avg_gain) if len(avg_gain) > 0 else 0
    avg_loss = abs(agg_func[agg_type](avg_loss)) if len(avg_loss) > 0 else 0.00000000001
    gl_ratio = (avg_gain)/(avg_loss)
    output_array[interval-1] = 100 - (100 / (1 + gl_ratio)) if scale else gl_ratio
    
    for t in range(interval, len(input_array)):        
        avg_gain = avg_gain*(interval-1)
        avg_loss = avg_loss*(interval-1)
        
        if(dxr[t] >= 0):
            avg_gain += dxr[t]
        else:
            avg_loss += abs(dxr[t])
            
        avg_gain = avg_gain/interval
        avg_loss = avg_loss/interval
        gl_ratio = (avg_gain)/(avg_loss)
        output_array[t] = 100 - (100 / (1 + gl_ratio)) if scale else gl_ratio
        
    return output_array

#MFI
def mfi(prices, volume, interval, scale=True):
    output_array = [50]*len(prices) if scale else [0]*len(prices)
    
    dx = ca.difference(prices, 1, 1)
    
    for t in range(interval-1, len(prices)):        
        pos_money_flow = sum([prices[x]*volume[x] for x in range(t-interval+1, t+1) if dx[x] > 0])
        neg_money_flow = sum([prices[x]*volume[x] for x in range(t-interval+1, t+1) if dx[x] < 0])
        neg_money_flow = abs(neg_money_flow) if neg_money_flow > 0 else 0.00000000001
        gl_ratio = (pos_money_flow)/(neg_money_flow)        
        output_array[t] = utils.clip(100 - (100 / (1 + gl_ratio)) if scale else gl_ratio, 0, 100)
        
    return output_array
#ATR
def average_true_range(closes, highs, lows, interval):
    true_ranges = [max([highs[x] - lows[x], abs(highs[x] - closes[x]), abs(closes[x] - lows[x])]) for x in range(len(closes))]
    return st.moving_average(true_ranges, interval)
