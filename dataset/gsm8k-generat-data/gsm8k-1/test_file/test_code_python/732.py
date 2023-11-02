def solution():
    """Boris has 100 apples. Beck has 23 fewer apples than Boris. If Boris gives Beck 10 apples, how many fewer apples does Beck have than Boris now?"""
    boris_apples = 100
    beck_apples = boris_apples - 23
    boris_apples -= 10
    beck_apples += 10
    difference = boris_apples - beck_apples
    result = difference
    return result

print(solution())