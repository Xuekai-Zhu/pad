def solution():
    """Julia had to make 6 cakes for the party. Each cake takes 12 minutes to mix and needs 9 more minutes to bake than mix. Then it takes 6 more minutes to cool and decorate than to bake. How many hours will it take to make all 6 cakes?"""
    cakes_to_make = 6
    mix_time = 12
    bake_time = mix_time + 9
    cool_decorate_time = bake_time + 6
    total_time_per_cake = mix_time + bake_time + cool_decorate_time
    total_time_all_cakes = total_time_per_cake * cakes_to_make
    hours_to_make = total_time_all_cakes / 60
    result = hours_to_make
    return result

print(solution())