def solution():
    touchdowns_worth = 7
    touchdowns_scored_by_bg = 7
    touchdowns_scored_by_cf = 9
    difference_in_score = touchdowns_scored_by_cf - touchdowns_scored_by_bg
    points = difference_in_score * touchdowns_worth
    result = points
    return result

print(solution())