def solution():
    # Calculate the total distance run by the other four members
    distance_other_members = 4 * 3  # four other members run 3 km each

    # Calculate the distance run by Ralph
    distance_Ralph = 2 * distance_other_members  # Ralph runs twice as much as any other member

    # Calculate the total distance of the race
    total_distance = distance_other_members + distance_Ralph

    result = total_distance
    return result

print(solution())