def solution():
    # Starting with 100 square inches
    square_inches = 100
    donated_inches = 0

    # Cut the cloth in half and donate half
    for i in range(2):
        cut_half = square_inches / 2
        donated_inches += cut_half
        square_inches = cut_half

    result = donated_inches
    return result

print(solution())