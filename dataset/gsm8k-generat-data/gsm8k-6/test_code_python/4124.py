def solution():
    # Calculate the amount of water each person can carry in one trip
    tina_pail = 4  # gallons
    tommy_pail = tina_pail + 2  # gallons
    timmy_pail = 2 * tommy_pail  # gallons

    # Calculate the total amount of water they can carry in three trips each
    total_water = (tina_pail + tommy_pail + timmy_pail) * 3  # gallons

    result = total_water
    return result

print(solution())