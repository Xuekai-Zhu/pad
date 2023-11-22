def solution():
    
    # Define the distance to the store and the speed of walking
    distance = 4
    speed = 4

    # Calculate the time it takes to walk to the store without walking back
    time_to_store = distance / speed

    # Calculate the time it takes to walk back home
    time_back_home = distance / speed

    # Calculate the total time it takes to reach the store
    total_time = time_to_store + time_back_home

    # Display the total time
    result = total_time
    return result

print(solution())