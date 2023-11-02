def solution():
    """A local school is holding a food drive.  Mark brings in 4 times as many cans as Jaydon.  Jaydon brings in 5 more than twice the amount of cans that Rachel brought in.  If there are 135 cans total, how many cans did Mark bring in?"""
    # Let's say Rachel brought in x cans
    # Then, Jaydon brought in 2x + 5 cans
    # And Mark brought in 4(2x+5) = 8x + 20 cans
    # The total number of cans is 135, so we can create an equation:
    # x + 2x + 5 + 8x + 20 = 135
    # Simplifying the equation, we get:
    # 11x + 25 = 135
    # Solving for x, we get:
    # x = 10
    # Therefore, Rachel brought in 10 cans, Jaydon brought in 2(10) + 5 = 25 cans, and Mark brought in 8(10) + 20 = 100 cans

    # Calculate the number of cans Mark brought in
    mark_cans = 100

    # Display the number of cans Mark brought in
    result = mark_cans
    return result

print(solution())