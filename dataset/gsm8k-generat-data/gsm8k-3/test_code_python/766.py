def solution():
    """Megan is delivering meals on wheels. Out of her 30 clients, 7 need vegan meals, 8 need kosher meals, and three people need meals that are both vegan and kosher. How many meals does Megan deliver that are neither kosher nor vegan?"""
    # Define the number of clients who need vegan meals, kosher meals, and both
    vegan = 7
    kosher = 8
    both = 3

    # Calculate the number of clients who need neither kosher nor vegan meals
    neither = 30 - (vegan + kosher - both)

    # Calculate the total number of meals that Megan delivers that are neither kosher nor vegan
    total = neither

    return total

print(solution())