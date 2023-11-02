def solution():
    """Every day, Wendi feeds each of her chickens three cups of mixed chicken feed, containing seeds, mealworms and vegetables to help keep them healthy. She gives the chickens their feed in three separate meals. In the morning, she gives her flock of chickens 15 cups of feed. In the afternoon, she gives her chickens another 25 cups of feed. How many cups of feed does she need to give her chickens in the final meal of the day if the size of Wendi's flock is 20 chickens?"""
    chickens = 20
    cups_per_meal = chickens * 3
    morning_meal = 15
    afternoon_meal = 25
    remaining_feed = cups_per_meal - morning_meal - afternoon_meal
    result = remaining_feed
    return result

print(solution())