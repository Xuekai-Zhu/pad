def solution():
    # Let's call the number of homework points "x"
    # We know that quiz points = homework points + 5, and test points = 4 * quiz points
    quiz_points = x + 5
    test_points = 4 * quiz_points

    # The total points assigned is 265
    total_points = x + quiz_points + test_points

    # We can set up an equation to solve for x:
    # x + (x+5) + (4*(x+5)) = 265
    # Solving for x, we get:
    x = 37

    result = x
    return result

print(solution())