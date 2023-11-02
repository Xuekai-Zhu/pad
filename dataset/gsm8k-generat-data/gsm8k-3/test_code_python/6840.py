def solution():
    """Bob started out the week with $80. On Monday alone, he spent half the money. On Tuesday, he spent one-fifth of the amount left from Monday. On Wednesday, he spent 3/8ths of the amount left from Tuesday. How much does he have left now?"""
    # Define Bob's starting amount
    starting_amount = 80

    # Calculate how much Bob spent on Monday
    monday_spending = starting_amount / 2

    # Calculate how much Bob had left after Monday
    tuesday_amount = starting_amount - monday_spending

    # Calculate how much Bob spent on Tuesday
    tuesday_spending = tuesday_amount / 5

    # Calculate how much Bob had left after Tuesday
    wednesday_amount = tuesday_amount - tuesday_spending

    # Calculate how much Bob spent on Wednesday
    wednesday_spending = wednesday_amount * 3 / 8

    # Calculate how much Bob has left
    total_spending = monday_spending + tuesday_spending + wednesday_spending
    remaining_amount = starting_amount - total_spending

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())