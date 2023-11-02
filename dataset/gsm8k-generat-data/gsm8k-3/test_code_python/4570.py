def solution():
    """Tom receives a $12 allowance per month. In the first week, he spends a third of it; in the second week, he spends a quarter of what he has left. How much money does he have left to finish the month?"""
    # Define the amount of Tom's allowance
    ALLOWANCE = 12

    # Calculate the amount Tom spends in the first week
    week1_spending = ALLOWANCE / 3

    # Calculate the amount Tom has left after the first week
    remaining_money = ALLOWANCE - week1_spending

    # Calculate the amount Tom spends in the second week
    week2_spending = remaining_money / 4

    # Calculate the amount Tom has left at the end of the second week
    total_remaining_money = remaining_money - week2_spending

    # Display the remaining amount of money
    result = total_remaining_money
    return result

print(solution())