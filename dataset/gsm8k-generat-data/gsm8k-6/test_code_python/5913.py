def solution():
    # Calculate the total time needed to make 1 cake
    mix_time = 12  # time to mix 1 cake
    bake_time = mix_time + 9  # time to bake 1 cake
    cool_time = bake_time + 6  # time to cool and decorate 1 cake
    total_cake_time = mix_time + bake_time + cool_time  # total time needed to make 1 cake

    # Calculate the total time needed to make 6 cakes
    total_time = total_cake_time * 6

    # Convert the time from minutes to hours
    hours = total_time / 60

    result = hours
    return result

print(solution())