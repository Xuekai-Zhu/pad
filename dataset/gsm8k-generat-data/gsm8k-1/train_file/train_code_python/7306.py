def solution():
    """Mark just got a new puppy that cost $10. He also bought enough food for 3 weeks. He knows the puppy eats 1/3 cup of food a day. A bag of food with 3.5 cups costs $2. How much did all of this cost him?"""
    puppy_cost = 10
    weeks_of_food = 3
    daily_food_amount = 1/3
    bag_size = 3.5
    bag_cost = 2
    total_food_amount = weeks_of_food * 7 * daily_food_amount
    bags_needed = total_food_amount / bag_size
    total_cost = puppy_cost + (bags_needed * bag_cost)
    result = total_cost
    return result

print(solution())