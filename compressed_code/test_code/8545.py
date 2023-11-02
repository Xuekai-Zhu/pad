def solution():
    
    households_visited = 20
    days_visited = 5
    half_households = households_visited / 2
    money_per_pair = 20 * 2
    money_collected = half_households * money_per_pair * days_visited
    result = money_collected
    return result

print(solution())