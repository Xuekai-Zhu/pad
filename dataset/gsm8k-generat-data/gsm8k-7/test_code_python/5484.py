def solution():
    # Let's assume the number of red marbles as x
    x = 1

    # Green marbles are 24 more than red marbles
    y = x + 24

    # Blue marbles are 5 times the number of red marbles
    z = 5 * x

    # As we know Brett has 24 more blue marbles than red marbles, thus
    y = z + 24

    # Solving we get
    x = 6
    result = x
    return result

print(solution())