def solution():
    first_half_mileage = 20
    second_half_mileage = 30
    num_weeks = 52 # Assume 52 weeks in a year

    # Calculate the total mileage for the first half of the year
    first_half_total = first_half_mileage * (num_weeks / 2)

    # Calculate the total mileage for the second half of the year
    second_half_total = second_half_mileage * (num_weeks / 2)

    # Calculate the total mileage for the whole year
    total_mileage = first_half_total + second_half_total
    result = total_mileage
    return result

print(solution())