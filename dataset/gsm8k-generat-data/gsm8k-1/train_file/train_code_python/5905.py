def solution():
    """Ralph is a member of the cross-country relay team. There are four other members on the team who run 3 km to complete their part of the race. Ralph runs twice as much as any member on his team to complete his part of the race. How long is the race?"""
    other_team_members = 4
    distance_per_member = 3
    ralph_distance = distance_per_member * 2
    total_distance = (other_team_members * distance_per_member) + ralph_distance
    result = total_distance
    return result

print(solution())