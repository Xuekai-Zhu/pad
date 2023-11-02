def solution():
    num_daughters = 3  # Grandma Olga has 3 daughters
    num_sons = 3  # Grandma Olga has 3 sons
    num_sons_daughters = num_sons * 5  # Each of her sons has 5 daughters
    num_daughters_sons = num_daughters * 6  # Each of her daughters has 6 sons

    # Calculate the total number of grandchildren
    total_grandchildren = (num_sons_daughters + num_daughters_sons)

    result = total_grandchildren
    return result

print(solution())