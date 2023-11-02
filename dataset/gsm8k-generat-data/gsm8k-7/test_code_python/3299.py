def solution():
    essays = 2
    essay_time = 60 # in minutes
    paragraphs = 5
    paragraph_time = 15 # in minutes
    total_time = 4 * 60 # in minutes

    # Calculate the total time used by the essays and paragraphs
    used_time = (essays * essay_time) + (paragraphs * paragraph_time)

    # Calculate the remaining time for short-answer questions
    remaining_time = total_time - used_time

    # Calculate the number of short-answer questions that can be assigned
    num_short_answers = remaining_time // 3
    result = num_short_answers
    return result

print(solution())