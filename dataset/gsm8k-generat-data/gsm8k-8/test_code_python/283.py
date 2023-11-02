def solution():
    # Calculate the total cost of the tickets
    total_cost = sum(range(1, 6))

    # Subtract the profit to get the prize money
    prize_money = total_cost - 4

    result = prize_money
    return result

print(solution())