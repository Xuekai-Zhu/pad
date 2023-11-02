def solution():
    xavier_in_six_years = 30
    six_years = 6
    ratio = 2

    # Calculate Xavier's age now
    xavier_now = xavier_in_six_years - six_years
    # Calculate Yasmin's age
    yasmin_now = xavier_now / ratio
    # Calculate the sum of their ages
    total_age = xavier_now + yasmin_now
    result = total_age
    return result

print(solution())