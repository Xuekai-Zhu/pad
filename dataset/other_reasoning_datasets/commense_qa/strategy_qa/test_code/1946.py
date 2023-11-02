def solution():
    box_length = 14
    box_width = 10
    box_depth = 5
    swan_length = 60 #inches
    if swan_length <= box_length and swan_length <= box_width and swan_length <= box_depth:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())