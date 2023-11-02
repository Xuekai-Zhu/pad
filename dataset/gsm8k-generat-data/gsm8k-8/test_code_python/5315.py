def solution():
    # Define the total distance Sam traveled
    total_distance = 18

    # Calculate the distance Sam walked in the grocery store
    grocery_store_distance = 2 * morning_run_distance

    # Calculate the sum of the morning run and grocery store distances
    morning_and_grocery_distance = morning_run_distance + grocery_store_distance

    # Calculate the distance Sam biked that evening
    evening_bike_distance = total_distance - morning_and_grocery_distance

    # Calculate the distance of Sam's morning run
    morning_run_distance = morning_and_grocery_distance - evening_bike_distance
    result = morning_run_distance
    return result

print(solution())