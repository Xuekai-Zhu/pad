def solution():
    first_half_mileage = 20  # Nicki ran 20 miles per week for the first half of the year
    second_half_mileage = 30  # Nicki increased her mileage to 30 miles per week for the second half of the year
    total_weeks = 52  # There are 52 weeks in a year

    # Calculate the total miles Nicki ran for the whole year
    total_mileage = (first_half_mileage * total_weeks / 2) + (second_half_mileage * total_weeks / 2)
    result = total_mileage
    return result

print(solution())