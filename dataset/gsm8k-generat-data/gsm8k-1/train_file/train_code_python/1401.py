def solution():
    """Dan is digging graves for a family killed by COVID-19. If it takes Dan 3 hours to dig an adult grave and 2 hours to dig a child's grave, how long does it take him to dig 5 adult graves and one child's grave?"""
    adult_grave_time = 3
    child_grave_time = 2
    num_adult_graves = 5
    num_child_graves = 1
    total_time = adult_grave_time * num_adult_graves + child_grave_time * num_child_graves 
    result = total_time
    return result

print(solution())