def solution():
    total_score = 810  # The team scored a total of 810 points
    second_bowler_score = total_score / (1 + 1/3 + 3)  # The second bowler scored 3 times as high as the third, and the first bowler scored 1/3 as many points as the second
    third_bowler_score = second_bowler_score / 3  # The second bowler scored 3 times as high as the third
    result = third_bowler_score
    return result

print(solution())