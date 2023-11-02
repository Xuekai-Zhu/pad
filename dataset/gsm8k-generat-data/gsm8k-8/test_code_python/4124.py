def solution():
    # Define the amount of water each person can carry in pail
    tina_pail = 4
    tommy_pail = tina_pail + 2
    timmy_pail = 2 * tommy_pail

    # Calculate the total amount of water carried per trip
    total_water_per_trip = tina_pail + tommy_pail + timmy_pail

    # Calculate the total amount of water filled in 3 trips
    water_filled = total_water_per_trip * 3

    result = water_filled
    return result

print(solution())