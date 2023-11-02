def solution():
    yuri_squares = 2 + 4 + 5  # total squares Yuri moved
    yuko_squares = 1 + 5  # total squares Yuko moved with first two dice
    # To be in front of Yuri, Yuko must move at least (yuri_squares + 1) squares
    # Subtracting total squares moved by Yuko so far gives us the value of the last die
    last_die_value = (yuri_squares + 1) - yuko_squares
    result = last_die_value
    return result

print(solution())