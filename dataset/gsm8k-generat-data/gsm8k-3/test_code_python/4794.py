def solution():
    """Yuko likes to play board games. He decides to play a game with his brother Yuri. They must roll 3 dice at the same time and move the squares corresponding to the value of the 3 dice. Yuri started and his dice had the following combination: 2, 4, and 5. On Yuko's turn, he rolled 1, 5, and X. How many squares must Yuko's last die move him so that he is in front of his brother?"""
    # Calculate Yuri's total score
    yuri_score = 2 + 4 + 5

    # Calculate the minimum score Yuko needs to beat Yuri
    min_score = yuri_score + 1

    # Calculate the maximum score Yuko can get with the first two dice
    max_score = 1 + 5 + 6

    # Calculate the minimum score Yuko needs to get with the third die
    min_last_die = min_score - max_score

    # Display the minimum score Yuko needs to get with the third die
    result = min_last_die
    return result

print(solution())