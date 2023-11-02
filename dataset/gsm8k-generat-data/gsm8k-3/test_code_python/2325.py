def solution():
    """George was selling some of his old toys on the internet. He managed to sell 3 little cars and a set of Legos. In total, he earned $45. How much did the Legos set cost, if one little car was sold for $5?"""
    # Define the cost of one little car
    LITTLE_CAR_COST = 5

    # Define the number of little cars sold
    little_cars_sold = 3

    # Calculate the total amount earned from selling the little cars
    little_cars_earned = little_cars_sold * LITTLE_CAR_COST

    # Calculate the cost of the Legos set
    legos_cost = 45 - little_cars_earned

    # Display the cost of the Legos set
    result = legos_cost
    return result

print(solution())