def solution():
    # Calculate Taro's score
    taro_score = ((3/5) * (30 * 5)) - 4  # 30 rounds, 5 points for each win, Taro's score is 3/5 of the total minus 4

    # Calculate the total score
    total_score = 30 * 5  # 30 rounds, 5 points for each win

    # Calculate Vlad's score
    vlad_score = total_score - taro_score

    result = vlad_score
    return result

print(solution())