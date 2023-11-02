def solution():
    """Ralph is a member of the cross-country relay team. There are four other members on the team who run 3 km to complete their part of the race. Ralph runs twice as much as any member on his team to complete his part of the race. How long is the race?"""
    # Define the distance run by each member of the team
    distance_run = 3
    
    # Define the distance run by Ralph
    ralph_distance = distance_run * 2
    
    # Calculate the total distance of the race
    total_distance = distance_run * 5 + ralph_distance
    
    result = total_distance
    return result

print(solution())