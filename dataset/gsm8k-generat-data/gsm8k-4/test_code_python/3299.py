def solution():
    """Karen is planning writing assignments for her fifth grade class. She knows each short-answer question takes 3 minutes to answer, each paragraph takes 15 minutes to write, and each essay takes an hour to write. If Karen assigns 2 essays and 5 paragraphs, how many short-answer questions should she assign if she wants to assign 4 hours of homework total?"""
    # Define the time it takes to complete each type of assignment
    SHORT_ANSWER_TIME = 3 # minutes
    PARAGRAPH_TIME = 15 # minutes
    ESSAY_TIME = 60 # minutes

    # Define the number of each type of assignment
    NUM_ESSAYS = 2
    NUM_PARAGRAPHS = 5

    # Define the total time available for homework
    TOTAL_TIME = 4*60 # 4 hours in minutes

    # Calculate the time used up by the essays and paragraphs
    time_used = (NUM_ESSAYS*ESSAY_TIME) + (NUM_PARAGRAPHS*PARAGRAPH_TIME)

    # Calculate the remaining time available for short-answer questions
    time_remaining = TOTAL_TIME - time_used

    # Calculate the number of short-answer questions that can be assigned in the remaining time
    num_short_answer = time_remaining // SHORT_ANSWER_TIME

    result = num_short_answer
    return result

print(solution())