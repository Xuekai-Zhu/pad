def solution():
    """Meryll wants to write 35 multiple-choice questions and 15 problem-solving questions for her Chemistry class. She already has written 2/5 of the multiple-choice and 1/3 of the problem-solving questions. How many more questions does she need to write for both multiple-choice and problem-solving?"""
    # Define the total number of multiple-choice and problem-solving questions needed
    MC_QUESTIONS_NEEDED = 35
    PS_QUESTIONS_NEEDED = 15

    # Define the number of multiple-choice and problem-solving questions already written
    MC_QUESTIONS_WRITTEN = round(2/5 * MC_QUESTIONS_NEEDED)
    PS_QUESTIONS_WRITTEN = round(1/3 * PS_QUESTIONS_NEEDED)

    # Calculate the number of multiple-choice and problem-solving questions still needed
    MC_QUESTIONS_STILL_NEEDED = MC_QUESTIONS_NEEDED - MC_QUESTIONS_WRITTEN
    PS_QUESTIONS_STILL_NEEDED = PS_QUESTIONS_NEEDED - PS_QUESTIONS_WRITTEN

    # Calculate the total number of questions still needed
    total_questions_still_needed = MC_QUESTIONS_STILL_NEEDED + PS_QUESTIONS_STILL_NEEDED

    # return the result
    result = total_questions_still_needed
    return result

print(solution())