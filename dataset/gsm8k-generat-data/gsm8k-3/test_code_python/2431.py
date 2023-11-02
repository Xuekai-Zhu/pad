def solution():
    """Justin and Sabrina at Pine Grove Elementary have 50 pencils combined. Justin has 8 more than twice as many pencils as Sabrina. How many pencils does Sabrina have?"""
    # Let x be the number of pencils Sabrina has
    # Then Justin has 8 more than twice as many, or 2x+8
    # The total number of pencils is x + (2x+8) = 3x+8, which we know is 50
    # Solving for x, we get:
    x = (50 - 8) / 3
    result = x
    return result

print(solution())