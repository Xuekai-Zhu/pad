def solution():
    # Define the time it takes to complete each type of assignment
    short_answer_time = 3
    paragraph_time = 15
    essay_time = 60

    # Define the number of each type of assignment
    num_essays = 2
    num_paragraphs = 5

    # Calculate the total time spent on essays and paragraphs
    total_essay_time = num_essays * essay_time
    total_paragraph_time = num_paragraphs * paragraph_time

    # Calculate the remaining time for short-answer questions
    remaining_time = 4 * 60 - total_essay_time - total_paragraph_time

    # Calculate the number of short-answer questions that can be assigned
    num_short_answers = remaining_time // short_answer_time
    result = num_short_answers
    return result

print(solution())