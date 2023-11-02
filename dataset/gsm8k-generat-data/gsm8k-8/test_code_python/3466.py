def solution():
    # Calculate the total points scored in the previous 24 games
    prev_total = 720

    # Calculate the average points per game in the previous 24 games
    avg_prev = prev_total / 24

    # Calculate the opponent's score in the championship game
    opp_score = (avg_prev / 2) - 2

    # Calculate UF's score in the championship game
    uf_score = prev_total + opp_score

    # Calculate the difference between UF's and the opponent's score
    diff = uf_score - opp_score

    result = opp_score
    return result

print(solution())