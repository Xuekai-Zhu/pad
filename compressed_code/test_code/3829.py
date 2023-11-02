def solution():
    
    pocket_money = 450
    chocolates_spending = pocket_money * (1/9)
    fruits_spending = pocket_money * (2/5)
    total_spending = chocolates_spending + fruits_spending
    remaining_money = pocket_money - total_spending
    result = remaining_money
    return result

print(solution())