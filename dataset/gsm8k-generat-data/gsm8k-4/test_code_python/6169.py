def solution():
    """Tomas is hoping to run a marathon next year, which is 26.3 miles. He knows that each month he trains, he can run twice as far as the month before. If he can run 3 miles during the first month of training, how many total months before the marathon should he start training to ensure he can run far enough?"""
    # Define the distance of the marathon
    marathon_distance = 26.3

    # Define the initial distance Tomas can run and initialize the month counter
    distance = 3
    months = 1

    # Continue training each month until Tomas can run the marathon distance
    while distance < marathon_distance:
        distance *= 2
        months += 1

    # Return the number of months
    result = months
    return result

print(solution())