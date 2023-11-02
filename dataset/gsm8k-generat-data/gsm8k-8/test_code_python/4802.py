def solution():
    # Define the amount of time it takes to vacuum each room
    time_per_room = 4
    
    # Define the number of rooms
    num_rooms = 5
    
    # Define the total amount of time needed to vacuum the whole house
    total_time = time_per_room * num_rooms
    
    # Define the battery life of the vacuum cleaner
    battery_life = 10
    
    # Calculate the number of times Mary needs to charge her vacuum cleaner
    num_charges = total_time // battery_life + 1
    
    result = num_charges
    return result

print(solution())