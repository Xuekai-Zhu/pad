def solution():
    # Define the number of apples Carla puts in her backpack
    starting_apples = 79
    
    # Define the number of apples lost due to Buffy and the hole
    lost_apples = Buffy_stole + 26
    
    # Calculate the number of apples Carla had at lunchtime
    remaining_apples = 8
    
    # Calculate the number of apples that Carla started with
    total_apples = starting_apples - lost_apples + remaining_apples
    
    # Calculate the number of apples Buffy stole
    Buffy_stole = total_apples - remaining_apples
    
    result = Buffy_stole
    return result

print(solution())