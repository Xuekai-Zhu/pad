def solution():
    # Let's assume the number of men and women in the office is x
    # Then, the number of women in the office before the meeting is (x/2)
    # Since 6 women were pulled from the office floor for the meeting, the new number of women in the office is (x/2) - 6
    # This is a 20% reduction from the original number of women, so we can set up the equation:
    # (x/2) - 6 = 0.8*(x/2)
    # Solving for x, we get:
    x = 60  # There are 60 people working in Ryan's office

    result = x
    return result

print(solution())