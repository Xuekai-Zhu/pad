def solution():
    
    monday_spending = 8
    tuesday_spending = monday_spending * 2
    wednesday_spending = tuesday_spending * 4
    total_spending = monday_spending + tuesday_spending + wednesday_spending
    money_left = 100 - total_spending
    result = money_left
    return result

print(solution())