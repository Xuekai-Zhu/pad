def solution():
    # Calculate Xavier's current age
    xavier_in_6_years = 30
    xavier_current = xavier_in_6_years - 6

    # Calculate Yasmin's current age
    yasmin_current = xavier_current / 2

    # Calculate the total of their current ages
    total_age = xavier_current + yasmin_current
    result = total_age
    return result

print(solution())