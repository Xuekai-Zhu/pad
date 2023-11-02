def solution():
    """Four students scored a total of 251 points in a board game. Naomi scored 68 of the points. 
    Yuri scored 10 more than half as many points as Naomi and Brianna scored 17 points more than Naomi. 
    How many points did Jojo score?"""
    
    total_points = 251
    naomi_points = 68
    yuri_points = (naomi_points / 2) + 10
    brianna_points = naomi_points + 17
    jojo_points = total_points - naomi_points - yuri_points - brianna_points
    result = jojo_points
    return result

print(solution())