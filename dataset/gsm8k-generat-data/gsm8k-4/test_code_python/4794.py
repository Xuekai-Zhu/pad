def solution():
    """Yuko likes to play board games. He decides to play a game with his brother Yuri. They must roll 3 dice at the same time and move the squares corresponding to the value of the 3 dice. Yuri started and his dice had the following combination: 2, 4, and 5. On Yuko's turn, he rolled 1, 5, and X. How many squares must Yuko's last die move him so that he is in front of his brother?"""

    # Define the squares moved by Yuri
    yuri_squares = 2 + 4 + 5

    # Define the squares moved by Yuko so far
    yuko_squares = 1 + 5

    # Calculate the minimum value of Yuko's last die to move him ahead of Yuri
    x_min = yuri_squares - yuko_squares + 1  # adding 1 to move Yuko ahead of Yuri

    result = x_min
    return result

print(solution())