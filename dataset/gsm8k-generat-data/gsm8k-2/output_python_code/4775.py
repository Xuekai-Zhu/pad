def solution():
    """Next year, there will be twice as many people going to the fair as are going this year, and the number of people who went to the fair last year was 200 less than those going next year. If the number of people going to the fair this year is 600, calculate the number of people at the fair in the three years."""
    current_year = 600
    next_year = 2 * current_year
    last_year = next_year - 200
    total = current_year + next_year + last_year
    result = total
    return result

print(solution())