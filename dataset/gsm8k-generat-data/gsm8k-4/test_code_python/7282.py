def solution():
    """Oliver has $40 and 200 quarters. If he gives his sister $5 and 120 quarters, how much money in total is he left with?"""
    # Define the starting amount of money and quarters
    starting_money = 40
    starting_quarters = 200

    # Define the amount of money and quarters given to Oliver's sister
    money_given = 5
    quarters_given = 120

    # Calculate the remaining amount of money and quarters
    remaining_money = starting_money - money_given
    remaining_quarters = starting_quarters - quarters_given

    # Calculate the total value of the remaining quarters
    quarters_value = remaining_quarters * 0.25

    # Calculate the total amount of money left
    remaining_total = remaining_money + quarters_value

    result = remaining_total
    return result

print(solution())