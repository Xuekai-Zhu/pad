def solution():
    """Terry spent 6$ for breakfast on Monday, twice as much on Tuesday, and on Wednesday Terry spent double what he did the previous two days combined.  How much did Terry spend total?"""
    # Define the spending on Monday
    monday_spending = 6

    # Define the spending on Tuesday
    tuesday_spending = 2 * monday_spending

    # Define the spending on Wednesday
    wednesday_spending = 2 * (monday_spending + tuesday_spending)

    # Calculate the total spending over the three days
    total_spending = monday_spending + tuesday_spending + wednesday_spending

    # Display the total spending
    result = total_spending
    return result

print(solution())