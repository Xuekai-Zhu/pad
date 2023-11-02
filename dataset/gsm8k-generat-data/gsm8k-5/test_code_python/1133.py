def solution():
    total_balloons = 100  # Marcus has 100 balloons
    water_per_balloon = 3  # Each balloon holds 3 ounces of water

    # Calculate the total amount of water in ounces needed
    total_water = total_balloons * water_per_balloon

    # Calculate the number of bottles of water needed
    bottles_needed = total_water / 50

    # Calculate the total cost of buying the water
    cost = bottles_needed * 2.5

    # Calculate the total amount paid by Marcus
    total_paid = 2 * 10 + 2 * 10

    # Calculate the change Marcus will receive
    change = total_paid - cost

    result = change
    return result

print(solution())