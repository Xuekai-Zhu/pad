def solution():
    """Julia had to make 6 cakes for the party. Each cake takes 12 minutes to mix and needs 9 more minutes to bake than mix. Then it takes 6 more minutes to cool and decorate than to bake. How many hours will it take to make all 6 cakes?"""
    # Define the time it takes to mix, bake, and decorate one cake
    mix_time = 12
    bake_time = mix_time + 9
    cool_time = bake_time + 6

    # Calculate the total time it takes to make one cake
    total_time = mix_time + bake_time + cool_time

    # Calculate the total time it takes to make 6 cakes
    total_time_6_cakes = total_time * 6

    # Convert the total time to hours
    hours = total_time_6_cakes / 60

    # Return the result
    result = round(hours, 2)
    return result

print(solution())