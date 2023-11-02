def solution():
    """Lyka wants to buy a smartphone worth $160 but she only has $40 at the moment. She plans to save an equal amount of money per week for two months for the remaining amount that she needs. How much should she save per week?"""
    # Define the initial amount of money Lyka has and the cost of the smartphone
    initial_money = 40
    smartphone_cost = 160

    # Calculate the remaining amount of money Lyka needs to save
    remaining_money = smartphone_cost - initial_money

    # Calculate the number of weeks in two months
    num_weeks = 8

    # Calculate the amount Lyka needs to save per week
    save_per_week = remaining_money / num_weeks

    # Return the result
    result = save_per_week
    return result

print(solution())