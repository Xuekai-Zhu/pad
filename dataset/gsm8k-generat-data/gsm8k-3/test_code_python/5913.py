def solution():
    """Julia had to make 6 cakes for the party. Each cake takes 12 minutes to mix and needs 9 more minutes to bake than mix. Then it takes 6 more minutes to cool and decorate than to bake. How many hours will it take to make all 6 cakes?"""
    # Define the time it takes to mix, bake, cool, and decorate one cake
    MIX_TIME = 12
    BAKE_TIME = MIX_TIME + 9
    COOL_DECORATE_TIME = BAKE_TIME + 6

    # Calculate the total time it takes to make all 6 cakes
    total_time = 6 * (MIX_TIME + BAKE_TIME + COOL_DECORATE_TIME)

    # Convert the total time to hours
    hours = total_time / 60

    # Display the total time in hours
    result = hours
    return result

print(solution())