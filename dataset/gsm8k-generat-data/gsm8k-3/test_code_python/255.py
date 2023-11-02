def solution():
    """A rectangular plot of private property is fenced in by a chain-link fence. The long sides of the plot are three times the length of the short sides. One short side of the fence is rusted from being hit by a sprinkler and needs to be replaced. If all the sides of the fence together are 640 feet long, how many feet of fence need to be replaced?"""
    # Let x be the length of the short side
    x = 1
    # Then the length of the long side is 3x
    long_side = 3 * x

    # The perimeter of the rectangular plot is:
    perimeter = 2 * (long_side + x)

    # We are given that the total length of the fence is 640 feet, so we can set up the equation:
    640 = perimeter - x

    # Solving for x, we get:
    x = (640 + 2 * long_side) / 5

    # Finally, we calculate the length of fence that needs to be replaced:
    fence_replaced = x

    # Display the length of fence that needs to be replaced
    result = fence_replaced
    return result

print(solution())