def solution():
    """Rihanna has $50 to go to the supermarket. Rihanna bought 6 mangoes and 6 cartons of apple juice. Each mango cost $3 and each carton of apple juice cost $3. How much money does Rihanna have left?"""
    # Define the cost of each mango and each carton of apple juice
    MANGO_PRICE = 3
    APPLE_JUICE_PRICE = 3

    # Define the number of mangoes and cartons of apple juice purchased
    mangoes = 6
    apple_juice = 6

    # Calculate the total cost of the mangoes
    mango_cost = mangoes * MANGO_PRICE

    # Calculate the total cost of the cartons of apple juice
    apple_juice_cost = apple_juice * APPLE_JUICE_PRICE

    # Calculate the total cost of all the items purchased
    total_cost = mango_cost + apple_juice_cost

    # Calculate the amount of money Rihanna has left
    money_left = 50 - total_cost

    # Display the amount of money Rihanna has left
    result = money_left
    return result

print(solution())