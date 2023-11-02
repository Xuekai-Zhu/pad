def solution():
    
    initial_count = 90
    samantha_took = 24
    shelby_ate = 12
    total_removed = samantha_took + shelby_ate
    refill_amount = total_removed / 2
    remaining_count = initial_count - total_removed + refill_amount
    result = remaining_count
    return result

print(solution())