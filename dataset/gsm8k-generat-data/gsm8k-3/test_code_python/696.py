def solution():
    """Every morning, Carla puts 79 apples in her backpack to eat for lunch. Unfortunately, Buffy stole some of Carla's apples on the school bus, and 26 apples fell out of a hole on the bottom. So at lunchtime, Carla only had 8 apples remaining. How many apples did Buffy steal from Carla?"""
    
    # Define the number of apples Carla puts in her backpack every morning
    starting_apples = 79
    
    # Define the number of apples that fell out of the hole on the bottom of the backpack
    lost_apples = 26
    
    # Define the number of apples Carla had left at lunchtime
    remaining_apples = 8
    
    # Calculate the number of apples Buffy stole
    stolen_apples = starting_apples - remaining_apples - lost_apples
    
    # Display the number of apples Buffy stole
    result = stolen_apples
    return result

print(solution())