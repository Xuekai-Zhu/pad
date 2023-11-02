def solution():
    """Terry spent 6$ for breakfast on Monday, twice as much on Tuesday, and on Wednesday Terry spent double what he did the previous two days combined. How much did Terry spend total?"""
    # Define the amount spent on Monday
    monday_spending = 6

    # Define the amount spent on Tuesday
    tuesday_spending = monday_spending * 2

    # Define the total spent on Monday and Tuesday
    total_spent = monday_spending + tuesday_spending

    # Define the amount spent on Wednesday
    wednesday_spending = total_spent * 2

    # Calculate the total amount spent
    total = monday_spending + tuesday_spending + wednesday_spending

    result = total
    return result

print(solution())