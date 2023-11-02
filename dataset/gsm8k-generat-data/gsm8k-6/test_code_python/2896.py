def solution():
    # Calculate the weight of each cut piece
    log_length = 20  # length of the log in feet
    log_weight_per_foot = 150  # weight of the log per linear foot
    cut_length = log_length / 2  # length of each cut piece
    cut_weight = cut_length * log_weight_per_foot  # weight of each cut piece
    result = cut_weight
    return result

print(solution())