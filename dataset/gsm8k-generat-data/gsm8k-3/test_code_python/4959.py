def solution():
    """Meryll wants to write 35 multiple-choice questions and 15 problem-solving questions for her Chemistry class. She already has written 2/5 of the multiple-choice and 1/3 of the problem-solving questions. How many more questions does she need to write for both multiple-choice and problem-solving?"""
    # Define the number of multiple-choice and problem-solving questions Meryll has already written
    MC_QUESTIONS_WRITTEN = 2/5 * 35
    PS_QUESTIONS_WRITTEN = 1/3 * 15

    # Calculate how many more questions Meryll needs to write for both categories of questions
    mc_questions_needed = 35 - MC_QUESTIONS_WRITTEN
    ps_questions_needed = 15 - PS_QUESTIONS_WRITTEN
    total_questions_needed = mc_questions_needed + ps_questions_needed

    # Display how many more questions Meryll needs to write
    result = total_questions_needed
    return result

print(solution())