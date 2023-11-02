def solution():
    """Dan is digging graves for a family killed by COVID-19. If it takes Dan 3 hours to dig an adult grave and 2 hours to dig a child's grave, how long does it take him to dig 5 adult graves and one child's grave?"""
    # Define the time to dig an adult and child grave
    ADULT_TIME = 3
    CHILD_TIME = 2

    # Define the number of adult and child graves
    adult_graves = 5
    child_graves = 1

    # Calculate the total time to dig all the graves
    total_time = (ADULT_TIME * adult_graves) + (CHILD_TIME * child_graves)

    # Display the total time
    result = total_time
    return result

print(solution())