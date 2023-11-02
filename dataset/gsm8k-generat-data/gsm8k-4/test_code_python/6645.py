def solution():
    """Sandro has six times as many daughters as sons. If he currently has three sons, how many children does he have?"""
    # Define the current number of sons
    current_sons = 3

    # Calculate the current number of daughters
    current_daughters = current_sons * 6

    # Calculate the total number of children
    total_children = current_sons + current_daughters

    # return the result
    result = total_children
    return result

print(solution())