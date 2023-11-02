def solution():
    """Anthony keeps a bottle of vinegar in his cupboard for 2 years. Each year 20% of the vinegar evaporates. What percent of the vinegar is left after 2 years?"""
    initial_amount = 100
    evaporation_rate = 20
    remaining_amount = initial_amount * (1 - evaporation_rate/100) ** 2
    percentage_remaining = remaining_amount / initial_amount * 100
    result = percentage_remaining
    return result

print(solution())