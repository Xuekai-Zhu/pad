def solution():
    """A few friends are making a small movie.  They hire a few actors and that cost $1200.  They also get food for the 50 people there.  Each person gets $3 worth of food. Equipment rental costs twice as much as food and actors combined. They sold the movie for $10,000. How much profit did they make?"""
    # Define the cost of actors and food
    ACTORS_COST = 1200
    FOOD_COST_PER_PERSON = 3

    # Calculate the total cost of food
    food_cost = 50 * FOOD_COST_PER_PERSON

    # Calculate the total cost of equipment rental
    equipment_cost = 2 * (ACTORS_COST + food_cost)

    # Calculate the total cost of making the movie
    total_cost = ACTORS_COST + food_cost + equipment_cost

    # Calculate the profit from selling the movie
    profit = 10000 - total_cost

    result = profit
    return result

print(solution())