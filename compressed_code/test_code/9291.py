def solution():
    
    adult_count = 10
    child_count = 2
    adult_deposit = 3
    child_deposit = 1
    flat_deposit = 20
    total_deposit = flat_deposit + (adult_count * adult_deposit) + (child_count * child_deposit)
    result = total_deposit
    return result

print(solution())