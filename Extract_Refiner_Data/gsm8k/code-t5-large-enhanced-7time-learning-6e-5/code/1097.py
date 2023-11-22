def solution():
    
    # Define the total distance run
    total_distance = 52

    # Define the distance run by Amber
    amber_distance = 8

    # Calculate the distance run by Micah
    micah_distance = amber_distance * 3.5

    # Calculate the distance run by Ahito
    ahito_distance = total_distance - amber_distance - micah_distance

    # Display the distance run by Ahito
    result = ahito_distance
    return result

print(solution())