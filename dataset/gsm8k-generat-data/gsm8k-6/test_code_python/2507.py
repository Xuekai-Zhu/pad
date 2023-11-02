def solution():
    # Calculate the total time that Sadie and Ariana took for their sections
    time_Sadie = 2
    distance_Ariana = 6 * 0.5  # Ariana sprints for half an hour
    time_Ariana = 0.5
    time_Sadie_Ariana = time_Sadie + time_Ariana
    
    # Calculate the distance that Sarah ran
    distance_Sarah = 4 * (4.5 - time_Sadie_Ariana)
    
    # Calculate the total distance of the race
    total_distance = distance_Sadie + distance_Ariana + distance_Sarah
    result = total_distance
    return result

print(solution())