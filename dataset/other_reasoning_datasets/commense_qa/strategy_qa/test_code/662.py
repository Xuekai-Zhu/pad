def solution():
    hobbit_height = "very short"
    halfling_height = "half the size of a human"
    drow_height = "around five feet"
    if hobbit_height == halfling_height:
        hobbit_height_inches = 36
        drow_height_inches = 60
        if drow_height_inches > hobbit_height_inches:
            result = "yes"
        else:
            result = "no"
    else:
        result = "unknown"
    return result

print(solution())