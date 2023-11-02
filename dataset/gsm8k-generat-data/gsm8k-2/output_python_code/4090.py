def solution():
    """Ryan works in an office that has an even number of men and women working there. Ryan participates in a meeting composed of 4 men and 6 women who are pulled from the office floor. This reduces the number of women working on the office floor by 20%. How many people work at Ryan's office?"""
    # Let's assume the total number of people in Ryan's office is x
    # Since the number of men and women is even, we can write x = 2y where y is the number of men and women each
    # After the meeting, there are (y - 6) women left on the office floor
    # We know that (y - 6) is 80% of y, so we can write (y - 6) = 0.8y
    # Solving for y, we get y = 30
    # Therefore, the total number of people in Ryan's office is x = 2y = 60
    result = 60
    return result

print(solution())