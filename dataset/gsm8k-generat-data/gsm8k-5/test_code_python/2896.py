def solution():
    log_length = 20  # The log is 20 feet long
    half_log_length = log_length / 2  # The log is cut in half
    weight_per_foot = 150  # Each linear foot of the log weighs 150 pounds

    # Calculate the weight of each cut piece
    cut_piece_weight = half_log_length * weight_per_foot
    result = cut_piece_weight
    return result

print(solution())