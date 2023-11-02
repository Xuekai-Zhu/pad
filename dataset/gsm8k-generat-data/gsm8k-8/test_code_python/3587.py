def solution():
    # Calculate the number of dancers
    dancers = 140 / 4

    # Calculate the number of dancers who did NOT slow dance
    non_slow_dancers = dancers - 25

    result = non_slow_dancers
    return result

print(solution())