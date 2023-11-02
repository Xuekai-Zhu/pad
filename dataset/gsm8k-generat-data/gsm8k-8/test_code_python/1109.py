def solution():
    # Define the number of oranges Mike received
    mike_oranges = 3

    # Calculate the number of apples Matt received
    matt_apples = 2 * mike_oranges

    # Calculate the total number of fruits Mark received
    mark_total_fruits = mike_oranges + matt_apples

    # Calculate the total number of fruits the three children have
    total_fruits = mike_oranges + matt_apples + mark_total_fruits
    result = total_fruits
    return result

print(solution())