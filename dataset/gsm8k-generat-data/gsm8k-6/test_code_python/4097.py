def solution():
    # Find the number of poets and singers at the party
    poets = 120 + 50  # there are 50 more poets than tree huggers
    singers = 400 - (poets + 120)  # total number of students at the party is 400

    result = singers
    return result

print(solution())