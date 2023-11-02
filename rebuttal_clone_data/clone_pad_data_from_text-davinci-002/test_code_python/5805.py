def solution():
    initial_population = 684
    percent_increase = 25
    percent_decrease = 40
    increase_amount = initial_population * (percent_increase / 100)
    decrease_amount = initial_population * (percent_decrease / 100)
    current_population = initial_population + increase_amount - decrease_amount
    result = current_population
    
    return result

print(solution())