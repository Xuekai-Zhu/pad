def solution():
    # Define the amount of Joe's pocket money
    pocket_money = 450

    # Calculate the amount spent on chocolates
    chocolates_spent = pocket_money * (1/9)

    # Calculate the amount spent on fruits
    fruits_spent = pocket_money * (2/5)

    # Calculate the total amount spent
    total_spent = chocolates_spent + fruits_spent

    # Calculate the amount of money Joe has left
    money_left = pocket_money - total_spent
    result = money_left
    return result

print(solution())