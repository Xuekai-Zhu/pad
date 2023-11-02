def solution():
    """Dan is digging graves for a family killed by COVID-19. If it takes Dan 3 hours to dig an adult grave and 2 hours to dig a child's grave, how long does it take him to dig 5 adult graves and one child's grave?"""
    # Define the time it takes for Dan to dig an adult and a child's grave
    adult_time = 3
    child_time = 2

    # Calculate the total time it takes for Dan to dig 5 adult graves
    total_adult_time = adult_time * 5

    # Calculate the total time it takes for Dan to dig one child's grave
    total_child_time = child_time

    # Calculate the total time it takes for Dan to dig all graves
    total_time = total_adult_time + total_child_time

    # Return the result
    result = total_time
    return result

print(solution())