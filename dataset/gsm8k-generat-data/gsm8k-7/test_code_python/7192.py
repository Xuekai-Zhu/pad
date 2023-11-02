def solution():
    starting_deadlift = 300  # pounds
    age_at_start = 13  # years
    age_at_end = 18  # years
    percent_increase = 250  # as a percentage
    increase_amount = 100  # pounds

    # Calculate Bobby's deadlift at 18 years old
    percent_multiplier = percent_increase / 100
    new_deadlift = starting_deadlift * (2.5 + percent_multiplier) + increase_amount

    # Calculate the increase per year
    increase_per_year = (new_deadlift - starting_deadlift) / (age_at_end - age_at_start)
    result = increase_per_year
    return result

print(solution())