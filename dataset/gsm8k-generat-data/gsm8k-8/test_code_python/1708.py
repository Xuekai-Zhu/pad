def solution():
    # Calculate the total points scored by Mark's team
    mark_2_pointers = 25 * 2
    mark_3_pointers = 8 * 3
    mark_free_throws = 10
    mark_points = mark_2_pointers + mark_3_pointers + mark_free_throws

    # Calculate the total points scored by the opponents
    opp_2_pointers = 2 * mark_2_pointers
    opp_3_pointers = 0.5 * mark_3_pointers
    opp_free_throws = 0.5 * mark_free_throws
    opp_points = opp_2_pointers + opp_3_pointers + opp_free_throws

    # Calculate the total points scored by both teams
    total_points = mark_points + opp_points
    result = total_points
    return result

print(solution())