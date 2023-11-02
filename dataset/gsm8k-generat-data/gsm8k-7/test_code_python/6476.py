def solution():
    monday_spending = 60
    tuesday_spending = monday_spending * 4
    wednesday_spending = monday_spending * 5

    total_spending = monday_spending + tuesday_spending + wednesday_spending
    result = total_spending
    return result

print(solution())