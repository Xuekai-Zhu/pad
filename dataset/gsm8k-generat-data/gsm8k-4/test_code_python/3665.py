def solution():
    """A snack machine accepts only quarters. Candy bars cost ¢25, each piece of chocolate costs ¢75, and a pack of juice costs ¢50. How many quarters are needed to buy three candy bars, two pieces of chocolate, and one pack of juice?"""
    # Define the cost of each item in cents
    CANDY_BAR_COST = 25
    CHOCOLATE_COST = 75
    JUICE_COST = 50

    # Calculate the total cost of the items
    total_cost = (3 * CANDY_BAR_COST) + (2 * CHOCOLATE_COST) + JUICE_COST

    # Calculate the number of quarters needed
    quarters_needed = total_cost // 25

    result = quarters_needed
    return result

print(solution())