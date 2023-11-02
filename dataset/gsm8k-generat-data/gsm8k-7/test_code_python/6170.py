def solution():
    total_fuel = 60
    first_third = 0
    second_third = total_fuel / 3
    final_third = second_third / 2

    # Calculate the fuel used in the first third of the trip
    first_third = total_fuel - second_third - final_third
    result = first_third
    return result

print(solution())