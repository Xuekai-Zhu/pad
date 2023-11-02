def solution():
    children = 6
    apples_eaten = 8
    apples_sold = 7
    apples_left = 60
    apples_harvested = children * 15
    apples_total = apples_harvested - (apples_eaten + apples_sold)
    result = apples_total
    
    return result

print(solution())