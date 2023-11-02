def solution():
    time_per_short_answer = 3  # Each short-answer question takes 3 minutes to answer
    time_per_paragraph = 15  # Each paragraph takes 15 minutes to write
    time_per_essay = 60  # Each essay takes an hour (60 minutes) to write
    num_essays = 2  # Karen assigns 2 essays
    num_paragraphs = 5  # Karen assigns 5 paragraphs
    total_homework_time = 4*60  # Karen wants to assign 4 hours (240 minutes) of homework total

    # Calculate the total time spent on essays and paragraphs
    essay_time = num_essays * time_per_essay
    paragraph_time = num_paragraphs * time_per_paragraph
    total_time = essay_time + paragraph_time

    # Calculate the remaining time available for short-answer questions
    remaining_time = total_homework_time - total_time

    # Calculate the number of short-answer questions Karen should assign
    num_short_answers = remaining_time // time_per_short_answer
    result = num_short_answers
    return result

print(solution())