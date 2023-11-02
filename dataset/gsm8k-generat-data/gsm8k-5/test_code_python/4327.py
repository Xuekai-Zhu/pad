def solution():
    total_budget = 20  # Samuel and Kevin have a total budget of $20
    samuel_ticket = 14  # Samuel buys a ticket for $14
    samuel_food_drink = 6  # Samuel spends $6 on food and drinks
    kevin_ticket = total_budget - samuel_ticket - samuel_food_drink - 2  # Kevin spends $2 on drinks and uses the remaining budget for his ticket

    # Calculate how much Kevin spent on food
    kevin_food = total_budget - samuel_ticket - samuel_food_drink - kevin_ticket
    result = kevin_food
    return result

print(solution())