def solution():
    """A Burmese python that was 1.4 meters long swallowed a 50-centimeter alligator. After one week, the alligator was completely digested. If this snake continues to eat 50-centimeter-long alligators at a constant rate of one alligator per week, what is the maximum number of alligators that the snake can eat in 616 days?"""
    initial_length = 1.4   # meters
    initial_alligator_length = 0.5   # meters
    digestion_time = 7   # days
    alligators_per_week = 1
    days_in_616_days = 616
    weeks_in_616_days = days_in_616_days / 7
    remaining_time_to_digest = digestion_time - 1
    additional_length_per_week = initial_alligator_length / digestion_time
    length_per_week = initial_length + additional_length_per_week
    max_alligators = weeks_in_616_days * alligators_per_week
    result = max_alligators
    return result

print(solution())