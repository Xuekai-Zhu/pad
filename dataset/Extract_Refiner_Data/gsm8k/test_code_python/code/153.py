def solution():
    
    # Calculate the distance Blake runs back and forth
    blake_distance = 100 * 2 * 15

    # Calculate the distance Kelly runs back and forth
    kelly_distance = 40 * 2

    # Calculate the total distance run by each person
    blue_distance = blake_distance + kelly_distance

    # Calculate the time taken by each person to run the loser
    loser_time = 15 * 60

    # Calculate the difference in distance run by each person
    difference = loser_distance - blue_distance

    # Display the difference in distance run
    result = difference
    return result

print(solution())