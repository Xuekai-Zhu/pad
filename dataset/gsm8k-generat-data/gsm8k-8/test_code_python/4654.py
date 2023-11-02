def solution():
    # Define the total years of teaching between Tom and Devin
    total_years = 70

    # Define the relation between Devin's and Tom's years of teaching
    devin_to_tom_ratio = 0.5 - 5 / (2 * total_years)

    # Calculate Tom's years of teaching
    tom_years = total_years / (1 + devin_to_tom_ratio)

    result = tom_years
    return result

print(solution())