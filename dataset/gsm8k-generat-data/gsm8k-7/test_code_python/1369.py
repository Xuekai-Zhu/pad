def solution():
    total_score = 810

    # Let x be the third bowler's score
    # The second bowler scored 3 times as high as the third, so their score is 3x
    # The first bowler scored 1/3 as many points as the second, so their score is (1/3)(3x) = x
    # The total score is the sum of all three bowlers' scores
    # x + 3x + x = 810
    # 5x = 810
    # x = 162

    third_bowler_score = 162
    result = third_bowler_score
    return result

print(solution())