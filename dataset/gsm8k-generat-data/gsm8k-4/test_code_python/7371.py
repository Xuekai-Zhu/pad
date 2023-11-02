def solution():
    """Karen's students are about to take a standardized test. Karen gets a $500 bonus if their average score is above 75, plus an extra $10 bonus for every additional point the average score increases above 75. So far, Karen has graded 8 tests, and the average is 70. Given that each student can have a maximum score of 150, what combined score do the last two tests need to have for Karen to earn a $600 bonus?"""
    # Define the current average score and the number of tests
    current_average = 70
    num_tests = 8

    # Define the target average score and the bonus amount
    target_average = 75
    bonus_amount = 600

    # Determine the total current score
    current_total = current_average * num_tests

    # Determine the total score required for the desired bonus
    target_total = (target_average * (num_tests + 2)) - current_total - bonus_amount

    # Determine the combined score required for the last two tests
    last_two_tests = target_total / 2

    # Return the result
    result = last_two_tests
    return result

print(solution())