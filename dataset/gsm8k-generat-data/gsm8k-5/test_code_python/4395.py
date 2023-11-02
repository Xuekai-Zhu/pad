def solution():
    xavier_age_in_six_years = 30  # Xavier will be 30 in six years
    xavier_age_now = xavier_age_in_six_years - 6  # Calculate Xavier's current age
    yasmin_age_now = xavier_age_now / 2  # Yasmin is half as old as Xavier

    # Calculate the total of their ages now
    total_ages = xavier_age_now + yasmin_age_now
    result = total_ages
    return result

print(solution())