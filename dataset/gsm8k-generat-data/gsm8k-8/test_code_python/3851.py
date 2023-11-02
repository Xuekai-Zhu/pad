def solution():
    # Calculate the total distance Peter will travel
    total_distance = 2 * (1615 + 7019)

    # Calculate the distance he will travel between Germany and Russia
    germany_to_russia_distance = 7019 - 1615

    # Calculate the distance he will travel to get back to Spain from Russia
    russia_to_spain_distance = 7019

    # Calculate the total distance he will travel for the round trip
    round_trip_distance = germany_to_russia_distance + russia_to_spain_distance

    # Calculate the total distance he will have left to travel after the round trip
    remaining_distance = total_distance - round_trip_distance

    result = remaining_distance
    return result

print(solution())