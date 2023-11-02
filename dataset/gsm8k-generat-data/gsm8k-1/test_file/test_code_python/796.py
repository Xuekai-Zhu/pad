def solution():
    """Pierson scored 278 points in one game of bowling. Nikita scored 11 more than half as many as Pierson. How many points did Pierson and Nikita have in total?"""
    pierson_score = 278
    nikita_score = (pierson_score / 2) + 11
    total_score = pierson_score + nikita_score
    result = total_score
    return result

print(solution())