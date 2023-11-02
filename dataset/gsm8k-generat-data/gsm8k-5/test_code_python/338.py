def solution():
    total_distance = 2*(5+6)  # Bobby drives to the supermarket and back, then to the farm
    remaining_gasoline = 2  # Bobby has 2 gallons of gasoline left after all the trips

    # Calculate the distance traveled before going back home to retrieve tools
    first_leg_distance = 2 + 2  # Bobby drives 2 miles to the supermarket and 2 miles back home

    # Calculate the distance traveled after going back home to retrieve tools
    second_leg_distance = 6 + 2  # Bobby drives 6 miles to the farm and 2 miles back home

    # Calculate the distance traveled without going back home to retrieve tools
    total_distance_without_tool = total_distance - first_leg_distance + second_leg_distance

    # Calculate the rate of gasoline consumption
    rate_of_consumption = total_distance_without_tool / (12 - remaining_gasoline)
    result = rate_of_consumption
    return result

print(solution())