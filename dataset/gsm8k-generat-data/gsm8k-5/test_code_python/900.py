def solution():
    nuts_per_day = (2 * 30) + 20  # Two squirrels store 30 nuts each, and one squirrel stores 20 nuts
    days = 40  # The squirrels have been storing nuts for 40 days

    # Calculate the total number of nuts stored
    total_nuts = nuts_per_day * days
    result = total_nuts
    return result

print(solution())