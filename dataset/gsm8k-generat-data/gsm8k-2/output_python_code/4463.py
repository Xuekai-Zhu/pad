def solution():
    """A few friends are making a small movie. They hire a few actors and that cost $1200. They also get food for the 50 people there. Each person gets $3 worth of food. Equipment rental costs twice as much as food and actors combined. They sold the movie for $10,000. How much profit did they make?"""
    actor_cost = 1200
    food_cost = 50 * 3
    equipment_cost = 2 * (actor_cost + food_cost)
    total_cost = actor_cost + food_cost + equipment_cost
    revenue = 10000
    profit = revenue - total_cost
    result = profit
    return result

print(solution())