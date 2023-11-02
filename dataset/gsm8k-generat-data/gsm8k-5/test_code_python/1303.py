def solution():
    # Calculate the amount spent on Tuesday
    tuesday_spending = 2 * 6  # Twice as much as Monday's spending

    # Calculate the total spending so far
    total_spending = 6 + tuesday_spending

    # Calculate the spending on Wednesday
    wednesday_spending = 2 * total_spending  # Double the previous two days combined

    # Calculate the total spending for all three days
    total_spending = total_spending + wednesday_spending

    # Return the final amount spent
    result = total_spending
    return result

print(solution())