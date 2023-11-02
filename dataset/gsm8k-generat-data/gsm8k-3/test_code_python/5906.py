def solution():
    """Ralph is a member of the cross-country relay team. There are four other members on the team who run 3 km to complete their part of the race. Ralph runs twice as much as any member on his team to complete his part of the race. How long is the race?"""
    # Define the distance run by each member of the team
    TEAM_DISTANCE = 3

    # Calculate Ralph's distance
    ralph_distance = 2 * TEAM_DISTANCE

    # Calculate the total distance of the race
    total_distance = (4 * TEAM_DISTANCE) + ralph_distance

    # Display the total distance of the race
    result = total_distance
    return result

print(solution())