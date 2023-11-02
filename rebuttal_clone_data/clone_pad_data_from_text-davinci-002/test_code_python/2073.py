def solution():
    initial_ounces = 36
    ounces_eaten = 6
    remaining_ounces = initial_ounces - ounces_eaten
    ounces_per_pile = remaining_ounces / 3
    result = ounces_per_pile
    return result

print(solution())