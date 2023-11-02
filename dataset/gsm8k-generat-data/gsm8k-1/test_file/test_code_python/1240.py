def solution():
    """Audrey has to take two math tests to pass 6th grade. She must correctly answer 70% of the total questions to move on to the 7th grade. The first test has 70 questions and she gets 60% of them correct. The second test has 40 questions. How many questions does she need to get right on the second test to move onto the 7th grade?"""
    total_questions = 70 + 40
    total_needed = total_questions * 0.7
    correct_on_first_test = 70 * 0.6
    needed_on_second_test = total_needed - correct_on_first_test
    result = round(needed_on_second_test)
    return result

print(solution())