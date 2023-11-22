def solution():
    
    # Define the distance of the race
    race_distance = 100

    # Calculate the distance finley has left after felling back 5 spots
    remaining_distance = race_distance - 5

    # Calculate the distance finley has moved ahead before falling behind 3
    moved_distance = 2 + 3

    # Calculate the distance finley has left after going ahead 3 spots
    remaining_distance -= moved_distance

    # Calculate the distance finley has jumped ahead by adding 1 spot
    jumped_distance = 1

    # Calculate the final distance finley has left
    final_distance = remaining_distance + jumped_distance

    # Display the final distance finley has left
    result = final_distance
    return result

print(solution())