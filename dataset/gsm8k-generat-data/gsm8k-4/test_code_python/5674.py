def solution():
    """A Burmese python that was 1.4 meters long swallowed a 50-centimeter alligator. After one week, the alligator was completely digested. If this snake continues to eat 50-centimeter-long alligators at a constant rate of one alligator per week, what is the maximum number of alligators that the snake can eat in 616 days?"""
    # Define the length of the snake and the length of the first alligator
    snake_length = 1.4
    alligator_length = 0.5

    # Calculate the maximum number of alligators the snake can eat based on its growth rate and the available time
    maximum_alligators = int((616/7) - 1)

    result = maximum_alligators
    return result

print(solution())