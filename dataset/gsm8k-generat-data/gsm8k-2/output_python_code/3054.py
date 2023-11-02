def solution():
    """Anthony keeps a bottle of vinegar in his cupboard for 2 years. Each year 20% of the vinegar evaporates. What percent of the vinegar is left after 2 years?"""
    starting_amount = 100
    evaporated_amount = starting_amount * 0.2
    remaining_after_one_year = starting_amount - evaporated_amount
    remaining_after_two_years = remaining_after_one_year - (evaporated_amount * remaining_after_one_year / starting_amount)
    percent_remaining = remaining_after_two_years / starting_amount * 100
    result = percent_remaining
    return result

print(solution())