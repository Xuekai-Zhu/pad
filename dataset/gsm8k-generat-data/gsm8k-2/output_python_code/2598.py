def solution():
    """Amy bought a 15-foot spool of string to cut up into wicks for making candles. If she cuts up the entire string into an equal number of 6-inch and 12-inch wicks, what is the total number of wicks she will have cut?"""
    total_length = 15 * 12  # convert feet to inches
    short_wick_length = 6
    long_wick_length = 12
    # find the maximum number of wicks she can cut using the shorter length
    max_short_wicks = total_length // short_wick_length
    # divide the remaining length by the longer length to find the remaining wicks
    remaining_length = total_length % short_wick_length
    remaining_wicks = remaining_length // long_wick_length
    total_wicks = max_short_wicks + remaining_wicks
    result = total_wicks
    return result

print(solution())