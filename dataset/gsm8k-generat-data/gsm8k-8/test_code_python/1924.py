def solution():
    # Define the variables
    rounds = 30
    win_score = 5
    taro_score = (3/5) * (rounds * win_score) - 4

    # Calculate Vlad's score
    vlad_score = (rounds * win_score) - taro_score
    result = vlad_score
    return result

print(solution())