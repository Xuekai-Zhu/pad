def solution():
    # Calculate the total cost of tickets for the first year
    first_year_cost = 12 * 5  # Kate visited the museum once a month and the ticket price was $5

    # Calculate the total cost of tickets for the next 2 years
    next_two_years_cost = 2 * 4 * 7  # Kate visited the museum 4 times a year and the ticket price was $7

    # Calculate the total cost of all visits to the museum after 3 years
    total_cost = first_year_cost + next_two_years_cost
    result = total_cost
    return result

print(solution())