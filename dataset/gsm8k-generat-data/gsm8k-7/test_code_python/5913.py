def solution():
    num_cakes = 6
    mix_time = 12
    bake_time = mix_time + 9
    cool_decorate_time = bake_time + 6

    # Calculate total time to make one cake
    total_time_per_cake = mix_time + bake_time + cool_decorate_time

    # Calculate total time to make all cakes
    total_time = total_time_per_cake * num_cakes

    # Convert total time to hours
    total_hours = total_time / 60

    result = total_hours
    return result

print(solution())