def solution():
    initial_shells = 20
    shells_per_day = [5, 5, 5, 6]

    # Calculate the total number of shells found on vacation
    total_shells_found = sum(shells_per_day)

    # Add the initial shells to the total number of shells found
    total_shells = initial_shells + total_shells_found
    result = total_shells
    return result

print(solution())