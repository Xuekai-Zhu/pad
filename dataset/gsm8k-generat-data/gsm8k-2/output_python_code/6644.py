def solution():
    """Sandro has six times as many daughters as sons. If he currently has three sons, how many children does he have?"""
    num_sons = 3
    num_daughters = 6 * num_sons
    total_children = num_sons + num_daughters
    result = total_children
    return result

print(solution())