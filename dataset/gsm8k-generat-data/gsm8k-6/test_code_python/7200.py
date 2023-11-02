def solution():
    # Find the number of turtles Johanna has
    turtles_johanna = 21 - 5  

    # Find the number of turtles Owen has after 1 month
    turtles_owen = 21 * 2  

    # Find the number of turtles Johanna has after losing half and donating the rest to Owen
    turtles_johanna = turtles_johanna // 2  
    turtles_owen += turtles_johanna  

    result = turtles_owen
    return result

print(solution())