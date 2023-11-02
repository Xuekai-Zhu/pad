def solution():
    """Jenny lives 5000 feet from her school, and every day she walks home.  One day as she was walking home from school, she dropped 1 kernel of popcorn per 25 feet she walked.  Later that evening, a squirrel came and ate one-quarter of the popcorn Jenny had dropped on her way home.  If Jenny walks to school the following morning and counts the popcorn on the ground, what is the total number of popcorn kernels she will find remaining on the ground?"""
    # Calculate the total number of popcorn kernels dropped by Jenny
    kernels_dropped = 5000 // 25

    # Calculate the number of kernels left after the squirrel eats one quarter
    kernels_left = kernels_dropped - (kernels_dropped // 4)

    # Display the number of kernels left
    result = kernels_left
    return result

print(solution())