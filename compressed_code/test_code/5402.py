def solution():
    
    total_donuts = 50
    eaten_on_ride = 2
    taken_by_secretary = 4
    remaining_donuts = total_donuts - eaten_on_ride - taken_by_secretary
    remaining_donuts = remaining_donuts / 2
    result = int(remaining_donuts)
    return result

print(solution())