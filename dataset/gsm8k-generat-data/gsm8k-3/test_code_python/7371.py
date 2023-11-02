def solution():
    """Karen's students are about to take a standardized test. Karen gets a $500 bonus if their average score is above 75,
    plus an extra $10 bonus for every additional point the average score increases above 75. So far, Karen has graded 8 tests,
    and the average is 70. Given that each student can have a maximum score of 150, what combined score do the last two
    tests need to have for Karen to earn a $600 bonus?"""
    # Define the target bonus and base bonus
    TARGET_BONUS = 600
    BASE_BONUS = 500

    # Define the number of students and tests already graded
    NUM_STUDENTS = 8
    NUM_GRADED_TESTS = 8

    # Define the maximum score per student
    MAX_SCORE = 150

    # Define the current average score
    current_average = 70

    # Calculate the current total score
    current_total_score = current_average * NUM_STUDENTS

    # Calculate the current total bonus
    current_bonus = BASE_BONUS + max(0, current_average - 75) * 10

    # Calculate the target total score
    target_total_score = (TARGET_BONUS - BASE_BONUS) / 10 / NUM_STUDENTS + current_total_score

    # Calculate the combined score needed on the last two tests
    combined_score_needed = target_total_score - current_total_score - MAX_SCORE * 2

    # Display the combined score needed
    result = combined_score_needed
    return result

print(solution())