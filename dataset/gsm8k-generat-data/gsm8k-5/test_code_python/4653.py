def solution():
    # Let's assume the number of cans Rachel brought in is x
    # Then Jaydon brought in 5 more than twice that number, which is 2x + 5
    # And Mark brought in 4 times as many as Jaydon, which is 4(2x + 5) = 8x + 20 cans
    # Altogether, they brought in 135 cans, so we can write an equation:
    # x + 2x + 5 + 8x + 20 = 135
    # Simplifying and solving for x, we get:
    # 11x + 25 = 135
    # 11x = 110
    # x = 10
    # So Rachel brought in 10 cans, Jaydon brought in 2*10+5 = 25 cans, and Mark brought in 8*10+20 = 100 cans
    result = 100
    return result

print(solution())