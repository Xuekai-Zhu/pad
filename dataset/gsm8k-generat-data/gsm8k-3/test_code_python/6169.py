def solution():
    """Tomas is hoping to run a marathon next year, which is 26.3 miles. He knows that each month he trains, he can run twice as far as the month before. If he can run 3 miles during the first month of training, how many total months before the marathon should he start training to ensure he can run far enough?"""
    # Define the distance Tomas can run during the first month
    distance = 3

    # Define the distance of the marathon
    marathon_distance = 26.3

    # Define the number of months of training
    months = 1

    # While Tomas can't run the distance of the marathon yet
    while distance < marathon_distance:
        # Double the distance Tomas can run
        distance *= 2
        # Increase the number of months of training
        months += 1

    # Display the total number of months of training needed to run the marathon
    result = months
    return result

print(solution())