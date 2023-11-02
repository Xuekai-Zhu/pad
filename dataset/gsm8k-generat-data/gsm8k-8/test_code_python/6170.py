def solution():
    # Define the total amount of fuel Lydia has
    total_fuel = 60

    # Calculate the amount of fuel needed for the second third of the trip
    second_third_fuel = total_fuel / 3

    # Calculate the amount of fuel needed for the final third of the trip
    final_third_fuel = second_third_fuel / 2

    # Calculate the amount of fuel left for the first third of the trip
    first_third_fuel = total_fuel - second_third_fuel - final_third_fuel

    result = first_third_fuel
    return result

print(solution())