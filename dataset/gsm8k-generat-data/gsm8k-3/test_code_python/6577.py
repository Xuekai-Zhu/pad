def solution():
    """ Jimmy needs to score at least 50 points to pass to the next class. He earned 20 points for each of the 3 exams he wrote but lost 5 points during the school year for bad behavior. How many more points can Jimmy lose and still be able to pass the next class? """
    # Define the minimum passing score
    MIN_PASSING_SCORE = 50

    # Calculate Jimmy's total score
    total_score = 20 * 3 - 5

    # Calculate the minimum score Jimmy needs to pass
    min_passing_score = MIN_PASSING_SCORE - total_score

    # Display the number of points Jimmy can still lose and pass
    result = min_passing_score
    return result

print(solution())