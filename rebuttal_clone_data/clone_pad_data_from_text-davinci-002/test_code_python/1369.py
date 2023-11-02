def solution():
    total_points = 810
    bowler_1 = total_points / 3
    bowler_2 = bowler_1 * 3
    bowler_3 = total_points - bowler_1 - bowler_2
    result = bowler_3
    return result

print(solution())