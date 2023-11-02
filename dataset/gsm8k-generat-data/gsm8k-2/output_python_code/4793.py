def solution():
    """Yuko likes to play board games. He decides to play a game with his brother Yuri. They must roll 3 dice at the same time and move the squares corresponding to the value of the 3 dice. Yuri started and his dice had the following combination: 2, 4, and 5. On Yuko's turn, he rolled 1, 5, and X. How many squares must Yuko's last die move him so that he is in front of his brother?"""
    yuri_position = 2 + 4 + 5
    yuko_position = 1 + 5
    target_position = yuri_position + 1
    x = target_position - yuko_position
    result = x
    return result

print(solution())