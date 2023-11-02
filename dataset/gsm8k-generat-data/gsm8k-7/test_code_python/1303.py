def solution():
    monday_spending = 6
    tuesday_spending = monday_spending * 2
    wednesday_spending = (monday_spending + tuesday_spending) * 2

    total_spending = monday_spending + tuesday_spending + wednesday_spending
    result = total_spending
    return result

print(solution())