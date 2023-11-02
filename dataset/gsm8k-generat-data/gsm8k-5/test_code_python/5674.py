def solution():
    initial_length = 1.4  # Burmese python's initial length (in meters)
    digestion_time = 7  # Time taken to digest an alligator (in days)
    growth_per_week = 0.05  # Growth in length per week (5% of initial length)
    max_days = 616  # Maximum number of days the snake will continue eating alligators

    # Calculate the final length of the python after digestion of the initial alligator
    final_length = initial_length + (50 / 100)  # Adding the length of the alligator eaten (in meters)

    # Calculate the number of weeks the snake will eat alligators
    weeks = (max_days - digestion_time) / 7

    # Calculate the maximum number of alligators the snake can eat in the given time
    max_alligators = int(weeks)  # Python can eat one alligator per week
    for i in range(int(weeks)):
        final_length += final_length * growth_per_week  # The python grows by 5% every week
        if final_length >= 6:  # The python can no longer eat alligators longer than 6 meters
            max_alligators = i + 1
            break

    result = max_alligators
    return result

print(solution())