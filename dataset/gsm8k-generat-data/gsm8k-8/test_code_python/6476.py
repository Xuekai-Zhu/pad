def solution():
    # Calculate how much Geoff spent on sneakers on Monday
    monday_spending = 60 / 2
    # Calculate how much Geoff will spend on sneakers on Tuesday and Wednesday
    tuesday_spending = monday_spending * 4
    wednesday_spending = monday_spending * 5

    # Calculate the total spending over the three days
    total_spending = monday_spending + tuesday_spending + wednesday_spending
    result = total_spending
    return result

print(solution())