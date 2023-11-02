def solution():
    """Mark's basketball team scores 25 2 pointers, 8 3 pointers and 10 free throws.  Their opponents score double the 2 pointers but half the 3 pointers and free throws.  What's the total number of points scored by both teams added together?"""
    # Define the point values for each type of shot
    TWO_POINTER = 2
    THREE_POINTER = 3
    FREE_THROW = 1

    # Calculate Mark's team's total points
    mark_total = (25 * TWO_POINTER) + (8 * THREE_POINTER) + (10 * FREE_THROW)

    # Calculate Mark's opponent's total points
    opponent_2_pointers = 25 * 2
    opponent_3_pointers = 8 * 0.5 * 3
    opponent_free_throws = 10 * 0.5
    opponent_total = (opponent_2_pointers + opponent_3_pointers + opponent_free_throws)

    # Calculate the combined total points for both teams
    total_points = mark_total + opponent_total

    # Display the total points
    result = total_points
    return result

print(solution())