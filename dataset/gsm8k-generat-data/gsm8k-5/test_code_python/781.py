def solution():
    cost_life_journey = 100  # The cost of The Life Journey CD
    cost_day_life = 50  # The cost of A Day a Life CD
    cost_rescind = 85  # The cost of When You Rescind CD
    quantity = 3  # I bought 3 CDs of each type

    # Calculate the total cost of all the CDs
    total_cost = (cost_life_journey + cost_day_life + cost_rescind) * quantity

    result = total_cost
    return result

print(solution())