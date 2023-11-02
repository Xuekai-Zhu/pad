def solution():
    initial_length = 1.4 # meters
    initial_alligator_length = 0.5 # meters
    digestion_time = 7 # days
    growth_rate = 0.5 # meters per alligator
    total_days = 616

    # Calculate the maximum number of alligators the snake can eat
    max_alligators = 0
    current_length = initial_length
    while total_days > 0:
        # Check if the snake can eat an alligator
        if current_length >= initial_alligator_length + growth_rate * max_alligators:
            max_alligators += 1
            total_days -= digestion_time
        else:
            current_length += 0.1 # meters per day
            total_days -= 1

    result = max_alligators
    return result

print(solution())