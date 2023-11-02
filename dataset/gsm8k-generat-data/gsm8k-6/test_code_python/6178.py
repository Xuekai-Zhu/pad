def solution():
    # Find Ibrahim's total budget
    total_budget = 120 + 19 + 55 + 20  # budget = price of MP3 player + price of CD + savings + father's contribution
    
    # Find how much money Ibrahim still needs to buy both items
    remaining_money = total_budget - (120 + 19)  # remaining money = total budget - price of MP3 player - price of CD
    
    result = remaining_money
    return result

print(solution())