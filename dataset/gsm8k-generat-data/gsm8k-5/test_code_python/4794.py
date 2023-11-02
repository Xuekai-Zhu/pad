def solution():
    yuri_score = 2 + 4 + 5  # Yuri's current score
    yuko_score = 1 + 5  # Yuko's current score
    x = 18 - yuko_score - yuri_score  # X is the value of the third die that Yuko rolled
    squares_to_move = yuri_score - yuko_score + x  # Yuko needs to move this many squares to be in front of Yuri
    result = squares_to_move
    return result

print(solution())