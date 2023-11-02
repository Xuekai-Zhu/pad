def solution():
    """If Joe spent 1/9 of his pocket money of $450 on chocolates and 2/5 on fruits, how much money does he have left?"""
    # Define Joe's pocket money
    pocket_money = 450

    # Calculate the amount Joe spent on chocolates
    chocolates_spending = pocket_money / 9

    # Calculate the amount Joe spent on fruits
    fruits_spending = pocket_money * 2 / 5

    # Calculate the total amount Joe spent
    total_spending = chocolates_spending + fruits_spending

    # Calculate the amount of money Joe has left
    money_left = pocket_money - total_spending

    # Display the amount of money Joe has left
    result = money_left
    return result

print(solution())