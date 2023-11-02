def solution():
    rope_length = 20  # The rope is 20 meters long
    friend_cost = 2  # Sarah's friend wants to buy the rope for $2 a meter
    profit_per_meter = 1.5  # Sarah plans to use the profit to buy a new rope at the store cost $1.5 a meter

    # Calculate the total cost of buying the rope
    total_cost = friend_cost + profit_per_meter

    # Calculate the amount of money Sarah will have left over after buying the new rope
    money_left = rope_length - total_cost
    result = money_left
    return result

print(solution())