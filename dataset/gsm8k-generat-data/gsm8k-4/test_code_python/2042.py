def solution():
    """The PTA had saved $400 set aside after a fundraising event. They spent a fourth of the money on school supplies. Then they spent half of what was left on food for the faculty. How much money did they have left?"""
    # Define the initial amount of money saved by the PTA
    initial_money = 400

    # Calculate the amount of money spent on school supplies
    school_supplies_cost = initial_money / 4

    # Calculate the amount of money left after buying school supplies
    remaining_money = initial_money - school_supplies_cost

    # Calculate the amount of money spent on food for the faculty
    faculty_food_cost = remaining_money / 2

    # Calculate the amount of money left after buying faculty food
    money_left = remaining_money - faculty_food_cost

    # Return the result
    result = money_left
    return result

print(solution())