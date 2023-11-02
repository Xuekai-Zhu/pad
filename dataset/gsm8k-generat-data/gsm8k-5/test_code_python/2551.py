def solution():
    # Duke needs 17 more points to tie the record and ends up breaking it by 5 points
    points_needed = 17
    record_points = 257
    final_points = record_points + points_needed + 5

    # Duke made 5 free throws (5 points) and 4 regular baskets (8 points) in the final game
    final_point_total = 5 + (4 * 2)

    # Duke normally scores 2 three-pointers per game
    normal_three_pointers = 2

    # Calculate how many more three-pointers Duke scored in the final game compared to his normal amount
    final_three_pointers = (final_points - final_point_total) // 3
    more_three_pointers = final_three_pointers - normal_three_pointers
    result = more_three_pointers
    return result

print(solution())