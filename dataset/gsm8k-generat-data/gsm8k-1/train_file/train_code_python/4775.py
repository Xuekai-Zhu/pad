def solution():
    """Next year, there will be twice as many people going to the fair as are going this year, and the number of people who went to the fair last year was 200 less than those going next year. If the number of people going to the fair this year is 600, calculate the number of people at the fair in the three years."""
    this_year = 600
    next_year = 2 * this_year
    last_year = next_year - 200
    total_people = this_year + next_year + last_year
    result = total_people
    return result

print(solution())