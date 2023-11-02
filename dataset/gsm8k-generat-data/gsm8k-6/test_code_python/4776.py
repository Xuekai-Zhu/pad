def solution():
    # Calculate the number of people going to the fair next year
    next_year = 2 * 600

    # Calculate the number of people who went to the fair last year
    last_year = next_year - 200

    # Calculate the total number of people at the fair in the three years
    total_people = 600 + next_year + last_year

    result = total_people
    return result

print(solution())