def solution():
    producer_age_at_death = 79
    current_year = 2021
    producer_birth_year = current_year - producer_age_at_death
    potential_octogenarian_year = producer_birth_year + 80
    if potential_octogenarian_year <= current_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())