def solution():
    """Mark's basketball team scores 25 2 pointers, 8 3 pointers and 10 free throws. Their opponents score double the 2 pointers but half the 3 pointers and free throws. What's the total number of points scored by both teams added together?"""
    # Define the points earned for each type of shot for Mark's team
    TWO_POINTER_POINTS = 2
    THREE_POINTER_POINTS = 3
    FREE_THROW_POINTS = 1

    # Calculate the points earned by Mark's team
    mark_2_pointers = 25 * TWO_POINTER_POINTS
    mark_3_pointers = 8 * THREE_POINTER_POINTS
    mark_free_throws = 10 * FREE_THROW_POINTS
    mark_total_points = mark_2_pointers + mark_3_pointers + mark_free_throws

    # Calculate the points earned by the opponents
    opponent_2_pointers = 2 * 25
    opponent_3_pointers = 0.5 * 8 * THREE_POINTER_POINTS
    opponent_free_throws = 0.5 * 10 * FREE_THROW_POINTS
    opponent_total_points = opponent_2_pointers + opponent_3_pointers + opponent_free_throws

    # Calculate the total points scored by both teams
    total_points = mark_total_points + opponent_total_points

    # return the result
    result = total_points
    return result

print(solution())