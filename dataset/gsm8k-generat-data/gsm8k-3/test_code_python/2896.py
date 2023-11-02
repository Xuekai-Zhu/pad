def solution():
    """John takes a 20-foot log and cuts it in half.  If each linear foot of the log weighs 150 pounds how much does each cut piece weigh?"""
    # Define the weight per linear foot of the log
    WEIGHT_PER_FOOT = 150

    # Define the length of the log and the length of each cut piece
    log_length = 20
    cut_length = log_length / 2

    # Calculate the weight of each cut piece
    cut_weight = cut_length * WEIGHT_PER_FOOT

    # Display the weight of each cut piece
    result = cut_weight
    return result

print(solution())