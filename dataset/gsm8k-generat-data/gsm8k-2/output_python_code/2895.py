def solution():
    """John takes a 20-foot log and cuts it in half. If each linear foot of the log weighs 150 pounds how much does each cut piece weigh?"""
    log_length = 20
    linear_weight = 150
    cut_length = log_length / 2
    cut_weight = cut_length * linear_weight
    result = cut_weight
    return result

print(solution())