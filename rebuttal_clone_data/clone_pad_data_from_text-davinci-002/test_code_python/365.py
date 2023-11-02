def solution():
    runners = 8
    first_five = 5
    rest = runners - first_five
    time_first_five = 8
    time_rest = time_first_five + 2
    total_time = time_first_five * first_five + time_rest * rest
    result = total_time
    return result

print(solution())