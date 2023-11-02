def solution():
    cakes_to_make = 6  # Julia needs to make 6 cakes for the party
    mix_time_per_cake = 12  # Each cake takes 12 minutes to mix
    bake_time_per_cake = mix_time_per_cake + 9  # Each cake needs 9 more minutes to bake than mix
    cool_decorate_time_per_cake = bake_time_per_cake + 6  # Each cake takes 6 more minutes to cool and decorate than to bake

    # Calculate the total time to make all 6 cakes
    total_time = (mix_time_per_cake + bake_time_per_cake + cool_decorate_time_per_cake) * cakes_to_make
    # Convert total minutes to hours
    total_time_hours = total_time / 60
    result = total_time_hours
    return result

print(solution())