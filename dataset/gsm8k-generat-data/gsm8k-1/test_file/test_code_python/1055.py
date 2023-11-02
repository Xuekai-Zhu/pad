def solution():
    """Imma has 3 cats. She feeds her cats twice a day with 60 grams of cat food. How many days will 720 grams of cat food last?"""
    cats = 3
    feedings_per_day = 2
    grams_per_feeding = 60
    total_grams_per_day = cats * feedings_per_day * grams_per_feeding
    days_lasted = 720 / total_grams_per_day
    result = days_lasted
    return result

print(solution())