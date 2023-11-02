def solution():
    """
    A few friends are making a small movie. They hire a few actors and that cost $1200.
    They also get food for the 50 people there. Each person gets $3 worth of food.
    Equipment rental costs twice as much as food and actors combined.
    They sold the movie for $10,000. How much profit did they make?
    """
    actor_cost = 1200
    num_people = 50
    food_cost = num_people * 3
    equipment_rental_cost = (food_cost + actor_cost) * 2
    total_cost = actor_cost + food_cost + equipment_rental_cost
    sale_price = 10000
    profit = sale_price - total_cost
    result = profit
    return result

print(solution())