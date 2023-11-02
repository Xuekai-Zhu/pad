def solution():
    
    initial_bees = 80000
    current_bees = initial_bees
    days = 0
    while current_bees > initial_bees / 4:
        current_bees -= 1200
        days += 1
    result = days
    return result

print(solution())