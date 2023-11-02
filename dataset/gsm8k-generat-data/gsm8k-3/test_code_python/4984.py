def solution():
    """Bill and Joan both work for a library. 5 years ago, Joan had 3 times as much experience as Bill. Now she has twice as much experience as Bill. How many years of experience does Bill have now?"""
    # Let's assume Bill had x years of experience 5 years ago
    x = 5

    # Let's calculate how much experience Joan had 5 years ago
    y = 3 * x

    # Now we need to add 5 years to their experiences
    x += 5
    y += 5

    # We know that now Joan has twice as much experience as Bill
    # So we can set up an equation: y = 2 * x
    # Solving for x, we get x = y/2
    x = y/2

    # The final answer is the number of years of experience Bill has now
    result = x
    return result

print(solution())