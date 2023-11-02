def solution():
    """James buys 20 pounds of beef and half that much pork.  He uses 1.5 pounds of meat to make meals at his restaurant.  Each meal sells for $20.  How much money did he make?"""
    # Define the amount of beef and pork purchased
    beef = 20
    pork = beef / 2

    # Define the amount of meat used per meal
    meat_per_meal = 1.5

    # Calculate the number of meals that can be made
    total_meat = beef + pork
    num_meals = total_meat / meat_per_meal

    # Calculate the total revenue
    revenue = num_meals * 20

    # Display the total revenue
    result = revenue
    return result

print(solution())