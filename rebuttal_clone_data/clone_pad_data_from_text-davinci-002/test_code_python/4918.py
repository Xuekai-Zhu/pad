def solution():
    points_scored = 14
    points_scored_by_chandra = 2 * points_scored
    points_scored_by_akiko = points_scored + 4
    points_scored_by_michiko = points_scored / 2
    total_points_scored = points_scored_by_chandra + points_scored_by_akiko + points_scored_by_michiko + points_scored
    result = total_points_scored
    return result

print(solution())