def solution():
    # Calculate the time it takes to assemble and decorate the cake
    prep_time = 1 + 1  # 1 hour to assemble and 1 hour to decorate

    # Calculate the time it takes to bake the cake normally
    bake_time_normal = 1.5

    # Calculate the time it takes to bake the cake on a day when the oven fails
    bake_time_fail = 2 * bake_time_normal

    # Calculate the total time it takes to make the cake on a day when the oven fails
    total_time_fail = prep_time + bake_time_fail + 1

    result = total_time_fail
    return result

print(solution())