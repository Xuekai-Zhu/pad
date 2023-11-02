def solution():
    """Karen is planning writing assignments for her fifth grade class. She knows each short-answer question takes 3 minutes to answer, each paragraph takes 15 minutes to write, and each essay takes an hour to write. If Karen assigns 2 essays and 5 paragraphs, how many short-answer questions should she assign if she wants to assign 4 hours of homework total?"""
    time_per_short_answer = 3 / 60  # converted to hours
    time_per_paragraph = 15 / 60  # converted to hours
    time_per_essay = 1
    num_essays = 2
    num_paragraphs = 5
    total_time = 4  # hours
    time_spent_on_essays = num_essays * time_per_essay
    time_spent_on_paragraphs = num_paragraphs * time_per_paragraph
    remaining_time = total_time - time_spent_on_essays - time_spent_on_paragraphs
    num_short_answers = remaining_time / time_per_short_answer
    result = num_short_answers

    return result

print(solution())