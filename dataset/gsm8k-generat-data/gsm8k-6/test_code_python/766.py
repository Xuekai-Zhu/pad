def solution():
    # Calculate the number of clients who need both vegan and kosher meals
    both_meals = 3  

    # Calculate the number of clients who need only vegan meals
    vegan_meals = 7 - both_meals  

    # Calculate the number of clients who need only kosher meals
    kosher_meals = 8 - both_meals  

    # Calculate the number of clients who need neither kosher nor vegan meals
    neither_meals = 30 - vegan_meals - kosher_meals - both_meals  

    result = neither_meals
    return result

print(solution())