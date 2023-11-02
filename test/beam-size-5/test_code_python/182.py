def solution():
    # Calculate the total number of straw pieces distributed among the small rodents
    total_straw = 160

    # Calculate the number of straw pieces kept in equal groups
    equal_groups_straw = total_straw / 3

    # Calculate the number of straw pieces kept in hamsters
    hamster_straw = 10 * 5

    # Calculate the number of straw pieces distributed among the rabbits
    rabbits_straw = 20

    # Calculate the number of rats
    equal_groups_straw = equal_groups_straw / 6

    # Calculate the number of rats
    rats_straw = equal_groups_straw * equal_groups_straw
    result = rats_straw
    return result

print(solution())