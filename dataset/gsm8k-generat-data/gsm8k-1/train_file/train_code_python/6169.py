def solution():
    """Lydia has 60 liters of fuel for her road trip. She will use a third of her fuel for the second third of the trip and half that amount for the final third. How much fuel can she use in the first third of the trip?"""
    total_fuel = 60
    second_third = total_fuel / 3
    final_third = second_third / 2
    first_third = total_fuel - second_third - final_third
    result = first_third
    return result

print(solution())