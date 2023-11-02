def solution():
    num_kids = 140
    frac_dancers = 1/4
    num_slow_dancers = 25

    # Calculate the number of dancers
    num_dancers = num_kids * frac_dancers

    # Calculate the number of dancers who did not slow dance
    num_non_slow_dancers = num_dancers - num_slow_dancers
    result = num_non_slow_dancers
    return result

print(solution())