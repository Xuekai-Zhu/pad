def solution():
    adult_grave_time = 3
    child_grave_time = 2
    adult_graves = 5
    child_graves = 1
    total_graves = adult_graves + child_graves
    total_time = (adult_grave_time * adult_graves) + (child_grave_time * child_graves)
    result = total_time
    return result

print(solution())