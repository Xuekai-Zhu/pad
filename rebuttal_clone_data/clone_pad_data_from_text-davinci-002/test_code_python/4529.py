def solution():
    builders_needed = 6
    number_of_houses = 5
    number_of_floors = 6
    days_to_build = 30
    cost_per_day = 100
    total_cost = builders_needed * cost_per_day * days_to_build * number_of_houses * number_of_floors 
    result = total_cost
    return result

print(solution())