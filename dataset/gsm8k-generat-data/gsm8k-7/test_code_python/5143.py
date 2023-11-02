def solution():
    billy_age = 4
    my_age = billy_age * 4

    # Calculate how many years ago Billy was born
    years_since_billy_born = billy_age - 0  # Assuming Billy was born 0 years ago

    # Calculate my age when Billy was born
    my_age_when_billy_born = my_age - years_since_billy_born

    result = my_age_when_billy_born
    return result

print(solution())