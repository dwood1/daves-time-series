# Clip
def clip(value, min_val, max_val):
    return min_val if value < min_val else (max_val if value > max_val else value) 