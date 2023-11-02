def solution():
    time_since_writing = 150
    included_in_curriculum = True
    if time_since_writing > 100 and included_in_curriculum:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())