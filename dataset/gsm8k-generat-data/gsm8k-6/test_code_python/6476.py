def solution():
    # Calculate the total amount spent on sneakers over three days
    monday_spending = 60  # Geoff spent $60 on Monday
    tuesday_spending = 4 * monday_spending  # Geoff will spend 4 times as much on Tuesday
    wednesday_spending = 5 * monday_spending  # Geoff will spend 5 times as much on Wednesday
    total_spending = monday_spending + tuesday_spending + wednesday_spending
    result = total_spending
    return result

print(solution())