def solution():
    miles_run = 40
    miles_walked = (3/5) * miles_run
    miles_jogged = miles_walked / 5

    total_distance = miles_run + miles_walked + miles_jogged
    result = total_distance
    return result

print(solution())