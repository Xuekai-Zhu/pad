def solution():
    num_people = 6  # Brian is cooking for himself, his wife, his two kids, his parents, and his wife's parents
    servings_per_person = 2  # Each person is expected to eat 2 servings
    total_servings = num_people * servings_per_person  # Calculate the total number of servings required
    milk_per_serving = 0.5  # The recipe requires 1/2 a cup of milk per serving
    ml_per_serving = milk_per_serving * 250  # Convert the milk per serving to milliliters
    ml_required = total_servings * ml_per_serving  # Calculate the total amount of milk required

    # Calculate the number of 1L cartons of milk required
    cartons_required = ml_required / 1000
    result = cartons_required
    return result

print(solution())