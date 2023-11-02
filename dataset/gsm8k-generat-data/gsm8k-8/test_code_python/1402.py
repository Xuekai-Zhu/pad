def solution():
    # Define the time it takes to dig an adult and child grave
    adult_time = 3
    child_time = 2

    # Calculate the total time it takes to dig 5 adult graves
    adult_total_time = 5 * adult_time

    # Calculate the time it takes to dig one child's grave
    child_total_time = child_time

    # Calculate the total time it takes to dig 5 adult graves and one child's grave
    total_time = adult_total_time + child_total_time

    result = total_time
    return result

print(solution())