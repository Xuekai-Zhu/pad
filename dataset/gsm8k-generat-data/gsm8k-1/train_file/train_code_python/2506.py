def solution():
    """Sadie, Ariana and Sarah are running a relay race. Each part of the race is a different length and covers different terrain. It takes Sadie 2 hours to run through the forest at an average speed of 3 miles per hour. Ariana sprints across the open field on her section at 6 miles per hour for half an hour. If Sarah runs along the beach at four miles per hour and their total time for the race is four and half hours, what is the total distance of the race?"""
    sadie_time = 2
    sadie_speed = 3
    ariana_time = 0.5
    ariana_speed = 6
    sarah_speed = 4
    total_time = 4.5
    
    # calculate distance based on time and speed
    sadie_distance = sadie_time * sadie_speed
    ariana_distance = ariana_time * ariana_speed
    sarah_distance = (total_time - sadie_time - ariana_time) * sarah_speed
    
    # calculate total distance
    total_distance = sadie_distance + ariana_distance + sarah_distance
    result = total_distance
    
    return result

print(solution())