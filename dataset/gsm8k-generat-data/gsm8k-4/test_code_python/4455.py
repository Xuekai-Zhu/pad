def solution():
    """Abigail spent 60% of her money on food, and 25% of the remainder on her phone bill. After spending $20 on entertainment, she is left with $40. How much money did Abigail have initially?"""
    # Define the initial amount of money Abigail had
    initial_money = None

    # Define the percentage of money Abigail spent on food
    food_percentage = 0.6

    # Calculate the amount of money Abigail spent on food
    food_money = initial_money * food_percentage

    # Calculate the remainder of Abigail's money
    remainder_money = initial_money - food_money

    # Define the percentage of the remainder that Abigail spent on her phone bill
    phone_percentage = 0.25

    # Calculate the amount of money Abigail spent on her phone bill
    phone_money = remainder_money * phone_percentage

    # Calculate the remaining amount of money Abigail has
    remaining_money = initial_money - food_money - phone_money - 20

    # Use the remaining money to solve for the initial amount
    initial_money = remaining_money / 0.15

    result = initial_money
    return result

print(solution())