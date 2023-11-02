def solution():
    total_time = 130
    time_penguins = total_time / 8
    time_elephants = total_time / 13
    time_seals = total_time - time_penguins - time_elephants
    result = time_seals
    return result

print(solution())