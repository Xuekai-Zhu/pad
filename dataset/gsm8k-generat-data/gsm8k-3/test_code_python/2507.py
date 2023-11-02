def solution():
    """Sadie, Ariana and Sarah are running a relay race. Each part of the race is a different length and covers different terrain. It takes Sadie 2 hours to run through the forest at an average speed of 3 miles per hour. Ariana sprints across the open field on her section at 6 miles per hour for half an hour. If Sarah runs along the beach at four miles per hour and their total time for the race is four and half hours, what is the total distance of the race?"""
    # Calculate the distance Sadie ran in the forest
    sadie_distance = 3 * 2

    # Calculate the distance Ariana ran across the open field
    ariana_distance = 6 * 0.5

    # Calculate the time Sarah spent running along the beach
    sarah_time = 4.5 - 2 - 0.5

    # Calculate the distance Sarah ran along the beach
    sarah_distance = 4 * sarah_time

    # Calculate the total distance of the race
    total_distance = sadie_distance + ariana_distance + sarah_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())