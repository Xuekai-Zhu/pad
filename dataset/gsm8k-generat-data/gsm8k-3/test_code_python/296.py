def solution():
    """Phillip's mother asked him to go to the supermarket to buy some things and gave him $95, so he spent $14 on oranges, $25 on apples and $6 on candy. How much money does he have left?"""
    # Define the amount of money Phillip's mother gave him
    starting_money = 95

    # Define the amount of money Phillip spent
    spent_money = 14 + 25 + 6

    # Calculate the amount of money Phillip has left
    remaining_money = starting_money - spent_money

    # Display the amount of money Phillip has left
    result = remaining_money
    return result

print(solution())