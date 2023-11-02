def solution():
    
    total_cost = (6 * 2) + (2 * 5) + (2 * 3) + (2 * 4)
    num_bills = total_cost // 10
    if total_cost % 10 > 0:
        num_bills += 1

    result = num_bills
    return result

print(solution())