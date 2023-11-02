def solution():
    joshua_rocks = 80  # Joshua collected 80 rocks
    jose_rocks = joshua_rocks - 14  # Jose collected 14 fewer rocks than Joshua
    albert_rocks = jose_rocks + 20  # Albert collected 20 more rocks than Jose

    # Calculate the difference between the number of rocks collected by Albert and Joshua
    difference = albert_rocks - joshua_rocks
    result = difference
    return result

print(solution())