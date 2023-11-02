def solution():
    """Karen is planning writing assignments for her fifth grade class. She knows each short-answer question takes 3 minutes to answer, each paragraph takes 15 minutes to write, and each essay takes an hour to write. If Karen assigns 2 essays and 5 paragraphs, how many short-answer questions should she assign if she wants to assign 4 hours of homework total?"""
    essay_time = 60
    paragraph_time = 15
    short_answer_time = 3
    total_time = 4 * 60  # 4 hours in minutes
    total_assignment_time = (2 * essay_time) + (5 * paragraph_time)
    remaining_time = total_time - total_assignment_time
    num_short_answers = remaining_time // short_answer_time
    result = num_short_answers
    return result

print(solution())