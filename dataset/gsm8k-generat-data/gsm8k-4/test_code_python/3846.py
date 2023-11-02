def solution():
    """Jenny lives 5000 feet from her school, and every day she walks home. One day as she was walking home from school, she dropped 1 kernel of popcorn per 25 feet she walked. Later that evening, a squirrel came and ate one-quarter of the popcorn Jenny had dropped on her way home. If Jenny walks to school the following morning and counts the popcorn on the ground, what is the total number of popcorn kernels she will find remaining on the ground?"""
    # Define the distance from school to home, and the distance Jenny drops a kernel of popcorn
    school_to_home_distance = 5000
    popcorn_distance = 25

    # Calculate the number of popcorn kernels dropped by Jenny
    kernels_dropped = school_to_home_distance // popcorn_distance

    # Calculate the number of popcorn kernels remaining after the squirrel eats one-quarter
    remaining_kernels = kernels_dropped - (kernels_dropped // 4)

    result = remaining_kernels
    return result

print(solution())