def solution():
    """Alex has 4 pens in the first week of a month. Every week her pen collection doubles. How many more pens will Alex have than Jane if Jane will have 16 pens after a month?"""
    # Calculate the number of pens Alex has after a month
    alex_pens = 4 * 2**4

    # Calculate the number of pens Jane has after a month
    jane_pens = 16

    # Calculate the difference in pens between Alex and Jane
    pen_difference = alex_pens - jane_pens

    result = pen_difference
    return result

print(solution())