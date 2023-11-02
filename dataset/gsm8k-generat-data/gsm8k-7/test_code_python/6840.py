def solution():
    starting_amount = 80

    # Calculate the amount spent on Monday
    monday_spending = starting_amount / 2

    # Calculate the amount left after Monday
    left_after_monday = starting_amount - monday_spending

    # Calculate the amount spent on Tuesday
    tuesday_spending = left_after_monday / 5

    # Calculate the amount left after Tuesday
    left_after_tuesday = left_after_monday - tuesday_spending

    # Calculate the amount spent on Wednesday
    wednesday_spending = 3/8 * left_after_tuesday

    # Calculate the amount left after Wednesday
    left_after_wednesday = left_after_tuesday - wednesday_spending
    result = left_after_wednesday
    return result

print(solution())