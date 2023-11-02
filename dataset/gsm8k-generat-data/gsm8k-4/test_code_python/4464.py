def solution():
    """A few friends are making a small movie. They hire a few actors and that cost $1200. They also get food for the 50 people there. Each person gets $3 worth of food. Equipment rental costs twice as much as food and actors combined. They sold the movie for $10,000. How much profit did they make?"""
    # Define the cost of actors and food
    ACTOR_COST = 1200
    FOOD_PER_PERSON = 3
    NUM_PEOPLE = 50

    # Calculate the total cost of food
    food_cost = FOOD_PER_PERSON * NUM_PEOPLE

    # Calculate the total cost of actors and food
    total_cost = ACTOR_COST + food_cost

    # Calculate the cost of equipment rental
    rental_cost = total_cost * 2

    # Calculate the profit from selling the movie
    sales = 10000

    # Calculate the total revenue
    revenue = sales - total_cost - rental_cost

    # Return the profit
    result = revenue
    return result

print(solution())