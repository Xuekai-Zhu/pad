def solution():
    # Calculate the money spent on potatoes
    potatoes_cost = 6 * 2  # 6 kilos of potatoes for $2 per kilo

    # Calculate the money spent on tomatoes
    tomatoes_cost = 9 * 3  # 9 kilos of tomatoes for $3 per kilo

    # Calculate the money spent on cucumbers
    cucumbers_cost = 5 * 4  # 5 kilos of cucumbers for $4 per kilo

    # Calculate the money spent on bananas
    bananas_cost = 3 * 5  # 3 kilos of bananas for $5 per kilo

    # Calculate the total money spent
    total_spent = potatoes_cost + tomatoes_cost + cucumbers_cost + bananas_cost

    # Calculate the remaining money
    remaining_money = 500 - total_spent
    result = remaining_money
    return result

print(solution())