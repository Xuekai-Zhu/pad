def solution():
    """Ralph is a member of the cross-country relay team. There are four other members on the team who run 3 km to complete their part of the race. Ralph runs twice as much as any member on his team to complete his part of the race. How long is the race?"""
    other_members_distance = 3 * 4
    ralph_distance = 2 * other_members_distance
    total_distance = other_members_distance + ralph_distance
    result = total_distance
    return result

print(solution())