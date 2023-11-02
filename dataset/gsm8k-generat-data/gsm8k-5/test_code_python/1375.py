def solution():
    piglet_cost = 10 * 12  # $10 cost per month to feed each piglet until it is sold at 12 months
    pig_cost = 10 * 16  # $10 cost per month to feed each pig until it is sold at 16 months
    total_cost = (piglet_cost * 3) + (pig_cost * 3)  # Total cost to feed and raise all 6 pigs
    total_earnings = (300 * 3) + (300 * 3)  # Total earnings from selling fully grown pigs

    # Calculate the profit earned by the farmer
    profit = total_earnings - total_cost
    result = profit
    return result

print(solution())