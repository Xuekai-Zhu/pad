def solution():
    
    # Define the time it takes to make the cake batter and bake the cake
    batter_time = 20
    bake_time = 30

    # Define the time it takes to cool and frost the cake
    cool_time = 2 * 60 + 10
    frost_time = cool_time

    # Calculate the total time it takes to make the cake on the same day
    total_time = batter_time + bake_time + cool_time + frost_time

    # Calculate the latest time Jordan can start making the cake on the same day
    latest_time = 5 * 60 + total_time

    # Display the latest time
    result = latest_time
    return result

print(solution())