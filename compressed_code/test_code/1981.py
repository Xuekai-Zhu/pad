def solution():
    
    passengers = 4
    oranges_received = passengers
    planned_spending = 15
    orange_cost = 1.5
    actual_spending = planned_spending - (oranges_received * orange_cost)
    saved_money = planned_spending - actual_spending
    percentage_saved = (saved_money / planned_spending) * 100
    result = percentage_saved
    return result

print(solution())