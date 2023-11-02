def solution():
    initial_oranges = 10  # kilograms of oranges bought initially
    additional_oranges = 5  # kilograms of oranges added for the neighbor
    total_oranges = initial_oranges + additional_oranges  # total kilograms of oranges bought
    two_weeks_oranges = 2 * total_oranges  # estimated kilograms of oranges needed for two weeks
    total_oranges_three_weeks = total_oranges + two_weeks_oranges  # total kilograms of oranges needed for three weeks
    result = total_oranges_three_weeks
    return result

print(solution())