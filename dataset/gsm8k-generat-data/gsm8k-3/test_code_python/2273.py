def solution():
    """Andrea buys herself a pony for her 30th birthday. She pays $500/month to rent a pasture for it, $10 a day for food, and $60/lesson for two lessons a week. How much does she spend on her pony in a year?"""
    # Define the cost of pasture rent per year
    PASTURE_RENT_YEAR = 500 * 12

    # Define the cost of food per year
    FOOD_YEAR = 10 * 365

    # Define the cost of lessons per year
    LESSONS_YEAR = 60 * 2 * 52

    # Calculate the total cost per year
    total_cost = PASTURE_RENT_YEAR + FOOD_YEAR + LESSONS_YEAR

    # Display the total cost
    result = total_cost
    return result

print(solution())