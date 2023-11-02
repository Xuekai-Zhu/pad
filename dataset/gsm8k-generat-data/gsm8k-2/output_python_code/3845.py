def solution():
    """Jenny lives 5000 feet from her school, and every day she walks home. One day as she was walking home from school, she dropped 1 kernel of popcorn per 25 feet she walked. Later that evening, a squirrel came and ate one-quarter of the popcorn Jenny had dropped on her way home. If Jenny walks to school the following morning and counts the popcorn on the ground, what is the total number of popcorn kernels she will find remaining on the ground?"""
    total_distance = 5000
    popcorn_per_distance = 1/25
    total_popcorn = total_distance * popcorn_per_distance
    eaten_popcorn = total_popcorn / 4
    remaining_popcorn = total_popcorn - eaten_popcorn
    result = remaining_popcorn
    return result

print(solution())