def solution():
    """Ali has $480. He spent half of it on food, and then he spent a third of what was left on a pair of glasses. How much money did he have left?"""
    # Define the initial amount of money Ali had
    initial_amount = 480

    # Calculate the amount of money spent on food
    food_cost = initial_amount / 2

    # Calculate the amount of money remaining after buying food
    remaining_amount = initial_amount - food_cost

    # Calculate the amount spent on glasses
    glasses_cost = remaining_amount / 3

    # Calculate the amount of money remaining after buying glasses
    final_amount = remaining_amount - glasses_cost

    # Return the final amount of money Ali has left
    result = final_amount
    return result

print(solution())