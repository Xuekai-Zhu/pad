def solution():
    watermelon_puree = 500  # Carla uses 500 ml of watermelon puree
    cream = 100  # Carla uses 100 ml of cream
    total_volume = watermelon_puree + cream  # Total volume of ingredients
    serving_size = 150  # Each serving is 150 ml

    # Calculate the number of servings Carla can make
    servings = total_volume // serving_size
    result = servings
    return result

print(solution())