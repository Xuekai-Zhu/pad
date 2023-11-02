def solution():
    initial_hours = 12
    initial_amount = 5000
    remaining_hours = 14
    remaining_amount = initial_amount + (initial_amount * 0.2)
    total_hours = initial_hours + remaining_hours
    total_amount = (initial_hours * initial_amount) + (remaining_hours * remaining_amount)
    result = total_amount
    
    return result

print(solution())