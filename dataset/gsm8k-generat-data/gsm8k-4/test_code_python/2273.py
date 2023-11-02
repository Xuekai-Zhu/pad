def solution():
    """Andrea buys herself a pony for her 30th birthday. She pays $500/month to rent a pasture for it, $10 a day for food, and $60/lesson for two lessons a week. How much does she spend on her pony in a year?"""
    # Define the monthly and daily costs
    pasture_cost = 500
    food_cost = 10 * 365

    # Define the cost and frequency of lessons
    lesson_cost = 60 * 2 * 52

    # Calculate the total cost for the year
    total_cost = pasture_cost * 12 + food_cost + lesson_cost

    # Return the result
    return total_cost

print(solution())