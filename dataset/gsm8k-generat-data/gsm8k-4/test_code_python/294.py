def solution():
    """Phillip's mother asked him to go to the supermarket to buy some things and gave him $95, so he spent $14 on oranges, $25 on apples and $6 on candy. How much money does he have left?"""
    # Define the initial amount of money
    initial_money = 95

    # Define the amount spent on each item
    oranges = 14
    apples = 25
    candy = 6

    # Calculate the total amount spent
    total_spent = oranges + apples + candy

    # Calculate the remaining amount of money
    remaining_money = initial_money - total_spent

    result = remaining_money
    return result

print(solution())