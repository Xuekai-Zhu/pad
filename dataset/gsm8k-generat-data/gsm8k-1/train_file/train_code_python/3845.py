def solution():
    """Jenny lives 5000 feet from her school, and every day she walks home. One day as she was walking home from school, she dropped 1 kernel of popcorn per 25 feet she walked. Later that evening, a squirrel came and ate one-quarter of the popcorn Jenny had dropped on her way home. If Jenny walks to school the following morning and counts the popcorn on the ground, what is the total number of popcorn kernels she will find remaining on the ground?"""
    distance_to_school = 5000
    kernels_dropped_per_foot = 1/25
    total_kernels_dropped = kernels_dropped_per_foot * distance_to_school
    kernels_eaten_by_squirrel = total_kernels_dropped/4
    kernels_remaining = total_kernels_dropped - kernels_eaten_by_squirrel
    result = kernels_remaining
    return result

print(solution())