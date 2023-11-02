def solution():
    """If Joe spent 1/9 of his pocket money of $450 on chocolates and 2/5 on fruits, how much money does he have left?"""
    # Define the total pocket money
    total_money = 450

    # Calculate the amount spent on chocolates
    chocolates_spent = total_money * (1/9)

    # Calculate the amount spent on fruits
    fruits_spent = total_money * (2/5)

    # Calculate the total amount spent
    total_spent = chocolates_spent + fruits_spent

    # Calculate the remaining money
    remaining_money = total_money - total_spent

    result = remaining_money
    return result

print(solution())