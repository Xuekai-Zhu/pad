def solution():
    # Define the amount spent on Monday
    monday_spending = 6

    # Define the amount spent on Tuesday
    tuesday_spending = 2 * monday_spending

    # Define the total spent on Monday and Tuesday
    total_mon_tues_spending = monday_spending + tuesday_spending

    # Define the amount spent on Wednesday
    wednesday_spending = 2 * total_mon_tues_spending

    # Calculate the total amount spent over the three days
    total_spending = monday_spending + tuesday_spending + wednesday_spending
    result = total_spending
    return result

print(solution())