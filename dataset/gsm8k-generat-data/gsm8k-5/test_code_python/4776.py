def solution():
    # Number of people going to the fair this year
    this_year = 600

    # Number of people going to the fair next year
    next_year = 2 * this_year

    # Number of people who went to the fair last year
    last_year = next_year - 200

    # Total number of people at the fair in the three years
    total_people = this_year + next_year + last_year
    result = total_people
    return result

print(solution())