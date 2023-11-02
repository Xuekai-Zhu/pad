def solution():
    
    num_passengers = 4
    oranges_per_passenger = 1
    total_oranges = num_passengers * oranges_per_passenger
    cost_per_orange = 1.5
    money_saved = total_oranges * cost_per_orange
    percent_saved = (money_saved / 15) * 100
    result = percent_saved
    return result

print(solution())