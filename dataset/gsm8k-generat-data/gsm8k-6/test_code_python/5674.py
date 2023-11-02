def solution():
    # Calculate the number of weeks in 616 days
    weeks = 616//7

    # Calculate the maximum number of alligators that the snake can eat in the given time period
    length_of_snake = 1.4
    length_of_alligator = 0.5
    max_alligators = int((length_of_snake - 0.1)/length_of_alligator) # The snake needs to leave 10% space in its stomach for digestion
    max_alligators = min(max_alligators, weeks) # The snake can eat only as many alligators as the number of weeks
    result = max_alligators
    return result

print(solution())