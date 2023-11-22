def solution():
    
    # Define the number of questions in the test and the time taken to complete the first test
    questions = 75
    time_first_test = 8

    # Define the time taken to complete the second test
    time_second_test = 6

    # Calculate the number of questions completed in the first test
    questions_completed = time_first_test * 5

    # Calculate the number of questions completed in the second test
    questions_completed += time_second_test * 5

    # Calculate the total time taken to complete both tests
    total_time = time_first_test + time_second_test

    # Calculate the number of questions Mark had left incomplete
    questions_left = questions - total_time

    # Display the number of questions Mark had left incomplete
    result = questions_left
    return result

print(solution())