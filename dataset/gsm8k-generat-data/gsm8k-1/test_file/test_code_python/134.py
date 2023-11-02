def solution():
    """Mark took a test yesterday that consisted of 75 questions. He completed the test at a rate of 5 questions per hour. Today, he took another test of 100 questions at the same rate. If Mark had 8 hours to complete the first test and 6 hours to complete the second one, how many questions did he leave incomplete?"""
    first_test_questions = 75
    second_test_questions = 100
    questions_per_hour = 5
    first_test_time = 8
    second_test_time = 6
    completed_first_test = questions_per_hour * first_test_time
    completed_second_test = questions_per_hour * second_test_time
    total_questions_completed = completed_first_test + completed_second_test
    total_questions = first_test_questions + second_test_questions
    incomplete_questions = total_questions - total_questions_completed
    result = incomplete_questions
    return result

print(solution())