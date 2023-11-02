def solution():
    # Calculate the number of red and blue marbles collected by Mary
    jenny_red = 30
    mary_red = 2 * jenny_red
    anie_blue = 2 * 25
    mary_blue = anie_blue / 2
    anie_red = mary_red + 20
    total_blue = jenny_blue + mary_blue + anie_blue  # Jenny's blue marbles are not given in the question, so assuming she collected the same number of blue marbles as Mary
    result = total_blue
    return result

print(solution())