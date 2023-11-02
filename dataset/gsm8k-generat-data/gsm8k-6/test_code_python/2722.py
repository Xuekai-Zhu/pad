def solution():
    # Calculate the total distance Jim drives to and from work
    total_distance = 2 * 10  # 10 miles away from his house

    # Calculate the amount of gas used for the round trip to and from work
    gas_used = 12 - (2/3)*12  # 2/3 of a 12-gallon tank is left after the round trip

    # Calculate the miles per gallon Jim gets
    miles_per_gallon = total_distance / gas_used
    result = miles_per_gallon
    return result

print(solution())