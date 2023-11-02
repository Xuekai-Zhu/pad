def solution():
    # Let's represent the number of marbles Steve has as x
    # Sam has twice as many as Steve, so Sam has 2*x marbles
    # Sally has 5 less than Sam, so Sally has (2*x - 5) marbles

    initial_total = 2*x + (2*x - 5) + x  # Total number of marbles in the beginning
    initial_total -= 2*3 + 3  # Sam gives 3 marbles each to Sally and Steve, and keeps 8 marbles
    final_total = 8 + (2*x - 5) + (x+3)  # Sam has 8 marbles left, Sally has 3 more, and Steve has 3 more

    # We can use these two equations to solve for x
    # 2*x + (2*x - 5) + x = 2*x + (x+3) + 8
    # Simplifying gives x = 6

    # So Steve originally had 6 marbles
    # After receiving 3 more from Sam, Steve now has 9 marbles
    result = 9
    return result

print(solution())