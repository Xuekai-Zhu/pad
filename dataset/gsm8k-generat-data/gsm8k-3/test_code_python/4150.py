def solution():
    """Mrs. Thomson received an incentive worth $240. She spent 1/3 of the money on food and 1/5 of it on clothes. Then, she put in her savings account 3/4 of the remaining money. How much money did Mrs. Thomson save?"""
    # Define the amount of the incentive
    incentive = 240

    # Calculate the amount spent on food
    food_cost = incentive * (1/3)

    # Calculate the amount spent on clothes
    clothes_cost = incentive * (1/5)

    # Calculate the remaining amount after spending on food and clothes
    remaining_amount = incentive - food_cost - clothes_cost

    # Calculate the amount saved in the savings account
    savings = remaining_amount * (3/4)

    # Display the amount saved
    result = savings
    return result

print(solution())