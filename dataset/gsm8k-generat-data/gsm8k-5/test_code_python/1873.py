def solution():
    jeremy_age = 40
    sebastian_age = jeremy_age + 4  # Sebastian is 4 years older than Jeremy
    sophia_age = 150 - (jeremy_age + sebastian_age + 9)  # The sum of their ages in three years is 150

    # Calculate Sophia's age three years from now
    sophia_age_three_years = sophia_age + 3

    result = sophia_age_three_years
    return result

print(solution())