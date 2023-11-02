def solution():
    """A Burmese python that was 1.4 meters long swallowed a 50-centimeter alligator. After one week, the alligator was completely digested. If this snake continues to eat 50-centimeter-long alligators at a constant rate of one alligator per week, what is the maximum number of alligators that the snake can eat in 616 days?"""
    initial_length = 1.4
    initial_alligator_length = 0.5
    digest_time = 7
    remaining_time = 616 - 7
    growth_rate = 0.25 # meters per year
    maximum_length = initial_length + growth_rate * remaining_time / 365
    maximum_alligator_length = maximum_length - initial_length
    maximum_alligators = (maximum_alligator_length / initial_alligator_length) - 1
    result = int(maximum_alligators)
    return result

print(solution())