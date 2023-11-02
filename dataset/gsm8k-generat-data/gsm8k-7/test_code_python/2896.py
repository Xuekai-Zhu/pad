def solution():
    log_length = 20
    log_weight_per_foot = 150

    # Calculate the weight of the entire log
    total_weight = log_length * log_weight_per_foot

    # Calculate the weight of each cut piece
    cut_weight = total_weight / 2
    result = cut_weight
    return result

print(solution())