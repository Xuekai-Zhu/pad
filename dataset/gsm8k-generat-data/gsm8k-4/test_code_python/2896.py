def solution():
    """John takes a 20-foot log and cuts it in half. If each linear foot of the log weighs 150 pounds how much does each cut piece weigh?"""
    # Define the length of the log and the weight per foot
    log_length = 20
    weight_per_foot = 150

    # Calculate the weight of each half of the log
    half_log_weight = log_length * weight_per_foot / 2

    # Return the weight of each half of the log
    result = half_log_weight
    return result

print(solution())