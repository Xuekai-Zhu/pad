def solution():
    """Ali has $480. He spent half of it on food, and then he spent a third of what was left on a pair of glasses. How much money did he have left?"""
    # Define the initial amount Ali had
    initial_amount = 480

    # Calculate the amount spent on food
    food_spending = initial_amount / 2

    # Calculate the amount left after food spending
    left_after_food = initial_amount - food_spending

    # Calculate the amount spent on glasses
    glasses_spending = left_after_food / 3

    # Calculate the remaining amount
    remaining_amount = left_after_food - glasses_spending

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())