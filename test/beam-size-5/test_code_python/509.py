def solution():
    
    initial_money = 500
    clothes_spending = initial_money * 0.2
    remaining_money = initial_money - clothes_spending
    cds_spending = remaining_money * 0.25
    remaining_money -= cds_spending
    result = remaining_money
    return result

print(solution())