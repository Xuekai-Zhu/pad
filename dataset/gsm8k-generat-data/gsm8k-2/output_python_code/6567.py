def solution():
    """Aunt Gemma has four dogs. She feeds them with dog food twice a day. Each dog can consume 250 grams of food per meal. If aunt Gemma bought 2 sacks of dog food, each weighing 50 kilograms, how many days will those food last?"""
    dogs = 4
    meals_per_day = 2
    food_per_meal = 250/1000  # convert grams to kilograms
    total_food_per_day = dogs * meals_per_day * food_per_meal
    total_food = 2 * 50  # two 50-kg sacks of dog food
    days = total_food / total_food_per_day
    result = days
    return result

print(solution())