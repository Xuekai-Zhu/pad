def solution():
    # Define the total number of cakes needed and the number of cakes already produced
    total_cakes = 60
    cakes_produced = total_cakes / 2

    # Calculate the number of cakes left to produce and the amount baked on the first day
    cakes_left = total_cakes - cakes_produced
    first_day_bake = cakes_left/2

    # Calculate the remaining number of cakes to produce and the amount baked on the second day
    cakes_left = cakes_left - first_day_bake
    second_day_bake = cakes_left/3

    # Calculate the total number of cakes baked and the number of cakes left to produce
    total_bake = first_day_bake + second_day_bake
    cakes_left = cakes_left - second_day_bake

    result = cakes_left
    return result

print(solution())