def solution():
    # Calculate the amount of time spent shark hunting in hours
    shark_hunting_time = 5

    # Calculate the number of sharks seen during shark hunting
    sharks_seen = shark_hunting_time * 6

    # Calculate the total profit made from taking photos of the sharks
    photo_profit = sharks_seen * 15

    # Calculate the cost of the boat fuel during shark hunting
    fuel_cost = (shark_hunting_time * 50) / 2

    # Calculate the total profit made after subtracting the fuel cost
    total_profit = photo_profit - fuel_cost
    result = total_profit
    return result

print(solution())