def solution():
    """Amy bought a 15-foot spool of string to cut up into wicks for making candles. If she cuts up the entire string into an equal number of 6-inch and 12-inch wicks, what is the total number of wicks she will have cut?"""
    spool_length = 15   # feet
    inch_per_foot = 12
    wick_length1 = 6     # inches
    wick_length2 = 12    # inches
    total_length = spool_length * inch_per_foot   # total length of string in inches
    num_wicks1 = total_length // wick_length1   # number of 6-inch wicks
    num_wicks2 = total_length // wick_length2   # number of 12-inch wicks
    num_total_wicks = num_wicks1 + num_wicks2   # total number of wicks
    result = num_total_wicks
    return result

print(solution())