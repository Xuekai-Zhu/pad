def solution():
    # Calculate the cost of the rose bushes
    roses_total_cost = 6 * 75  # 6 rose bushes at 75 dollars each
    roses_for_him_cost = (6 - 2) * 75  # Mike only buys 4 rose bushes for himself

    # Calculate the cost of the tiger tooth aloes
    aloes_cost = 2 * 100  # 2 tiger tooth aloes at 100 dollars each

    # Calculate the total cost of plants for himself
    total_cost = roses_for_him_cost + aloes_cost
    result = total_cost
    return result

print(solution())