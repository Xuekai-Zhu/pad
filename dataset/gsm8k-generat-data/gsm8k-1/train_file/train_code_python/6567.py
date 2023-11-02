def solution():
    """Aunt Gemma has four dogs. She feeds them with dog food twice a day. Each dog can consume 250 grams of food per meal. If Aunt Gemma bought 2 sacks of dog food, each weighing 50 kilograms, how many days will those food last?"""
    number_of_dogs = 4
    meals_per_day = 2
    grams_per_meal = 250
    grams_per_day = number_of_dogs * meals_per_day * grams_per_meal
    kilograms_per_sack = 50
    grams_per_sack = kilograms_per_sack * 1000
    total_days = (grams_per_sack * 2) // grams_per_day
    result = total_days
    return result

print(solution())