def solution():
    total_cost = 150
    cost_of_gummy_bears = 2
    cost_of_chocolate_chips = 5
    number_of_gummy_bears = 10
    number_of_chocolate_chips = 20
    total_cost_of_gummy_bears_and_chocolate_chips = cost_of_gummy_bears * number_of_gummy_bears + cost_of_chocolate_chips * number_of_chocolate_chips
    cost_of_chocolate_bars = total_cost - total_cost_of_gummy_bears_and_chocolate_chips
    number_of_chocolate_bars = 10
    cost_of_one_chocolate_bar = cost_of_chocolate_bars / number_of_chocolate_bars
    result = cost_of_one_chocolate_bar
    
    return result

print(solution())