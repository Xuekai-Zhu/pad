def solution():
    """John takes a 20-foot log and cuts it in half. If each linear foot of the log weighs 150 pounds how much does each cut piece weigh?"""
    log_length = 20
    cut_length = log_length / 2
    weight_per_foot = 150
    weight_per_cut_piece = cut_length * weight_per_foot
    result = weight_per_cut_piece
    return result

print(solution())