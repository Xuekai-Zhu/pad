def solution():
    rabbits_in_cage = 13
    total_rabbits_in_cage_after_addition = rabbits_in_cage + 7
    jasper_rabbits_ratio = 3

    # Calculate the number of rabbits Jasper saw in the park
    jasper_rabbits = total_rabbits_in_cage_after_addition * jasper_rabbits_ratio

    result = jasper_rabbits
    return result

print(solution())