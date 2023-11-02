def solution():
    # Let x be the size of the second ball in feet
    # The size of the first ball is 0.5x and the size of the third ball is 1.5x
    # Joy used 27 feet of yarn for the third ball
    # She used x + 0.5x + 27 + 1.5x = 3x + 27 feet of yarn in total
    # Therefore, x = (27 - 0.5x) / 2.5
    # Solving for x, we get x = 10.8 feet of yarn

    result = round(10.8, 2)  # Round to two decimal places
    return result

print(solution())