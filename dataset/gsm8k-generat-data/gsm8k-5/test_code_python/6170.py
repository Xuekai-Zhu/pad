def solution():
    total_fuel = 60  # Lydia has 60 liters of fuel
    second_third = total_fuel / 3  # Lydia will use a third of her fuel in the second third of the trip
    final_third = second_third / 2  # Lydia will use half of the second third fuel for the final third of the trip
    first_third = total_fuel - second_third - final_third  # Lydia will use the rest of her fuel in the first third of the trip
    result = first_third
    return result

print(solution())