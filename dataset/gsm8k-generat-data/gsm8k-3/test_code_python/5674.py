def solution():
    """A Burmese python that was 1.4 meters long swallowed a 50-centimeter alligator.  After one week, the alligator was completely digested.  If this snake continues to eat 50-centimeter-long alligators at a constant rate of one alligator per week, what is the maximum number of alligators that the snake can eat in 616 days?"""
    # Calculate the length of the python in centimeters
    python_length = 1.4 * 100

    # Calculate the length of the first alligator in centimeters
    alligator_length = 50

    # Calculate the remaining length of the python after swallowing the first alligator
    remaining_length = python_length - alligator_length

    # Calculate the number of weeks in 616 days
    num_weeks = 616 // 7

    # Calculate the maximum number of alligators that the snake can eat in 616 days
    max_num_alligators = (remaining_length // 50) * num_weeks

    # Display the maximum number of alligators
    result = max_num_alligators
    return result

print(solution())