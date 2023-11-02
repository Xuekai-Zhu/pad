def solution():
    """Karen is planning writing assignments for her fifth grade class. She knows each short-answer question takes 3 minutes to answer, each paragraph takes 15 minutes to write, and each essay takes an hour to write. If Karen assigns 2 essays and 5 paragraphs, how many short-answer questions should she assign if she wants to assign 4 hours of homework total?"""
    # Define the time it takes to complete each type of assignment
    SHORT_ANSWER_TIME = 3 # in minutes
    PARAGRAPH_TIME = 15 # in minutes
    ESSAY_TIME = 60 # in minutes

    # Define the number of each type of assignment assigned
    num_essays = 2
    num_paragraphs = 5

    # Calculate the total time spent on essays
    essay_time = num_essays * ESSAY_TIME

    # Calculate the total time spent on paragraphs
    paragraph_time = num_paragraphs * PARAGRAPH_TIME

    # Calculate the total time spent on all assignments
    total_time = essay_time + paragraph_time

    # Calculate the remaining time for short-answer questions
    remaining_time = 4 * 60 - total_time

    # Calculate the number of short-answer questions that can be assigned
    num_short_answers = remaining_time // SHORT_ANSWER_TIME

    # Display the number of short-answer questions that can be assigned
    result = num_short_answers
    return result

print(solution())