def solution():
    """Jacob takes four tests in his physics class and earns 85, 79, 92 and 84. What must he earn on his fifth and final test to have an overall average of 85?"""
    # Define the number of tests and the desired average
    NUM_TESTS = 5
    DESIRED_AVERAGE = 85

    # Define the scores Jacob has received so far
    scores = [85, 79, 92, 84]

    # Calculate the total of Jacob's scores so far
    total_score = sum(scores)

    # Calculate the score Jacob needs on his final test
    desired_score = DESIRED_AVERAGE * NUM_TESTS - total_score

    # Display the score Jacob needs on his final test
    result = desired_score
    return result

print(solution())