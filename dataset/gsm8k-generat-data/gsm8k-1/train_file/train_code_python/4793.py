def solution():
    """Yuko and Yuri are playing a board game. They must roll 3 dice at the same time and move the squares corresponding to the value of the 3 dice. Yuri started and his dice had the following combination: 2, 4, and 5. On Yuko's turn, he rolled 1, 5, and X. How many squares must Yuko's last die move him so that he is in front of his brother?"""
    yuri_squares = 2 + 4 + 5
    yuko_squares = 1 + 5
    target_squares = yuri_squares + 1
    needed_squares = target_squares - yuko_squares
    result = needed_squares
    return result

print(solution())