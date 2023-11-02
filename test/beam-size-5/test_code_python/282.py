def solution():
    
    quarters = 5
    dimes = 2
    total_cents = (quarters * 25) + (dimes * 10)
    pop_cost = 55
    remaining_cents = total_cents - pop_cost
    result = remaining_cents
    return result

print(solution())