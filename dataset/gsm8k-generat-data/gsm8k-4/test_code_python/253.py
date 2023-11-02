def solution():
    """A rectangular plot of private property is fenced in by a chain-link fence. The long sides of the plot are three times the length of the short sides. One short side of the fence is rusted from being hit by a sprinkler and needs to be replaced. If all the sides of the fence together are 640 feet long, how many feet of fence need to be replaced?"""
    # Let x be the length of the short side of the fence
    x = None

    # Calculate the length of the long side of the fence
    y = 3 * x

    # Calculate the total length of the fence
    total_length = 2 * x + 2 * y

    # Solve for x by setting the total length equal to 640 feet
    x = (640 - 2 * y) / 4

    # Calculate the length of the rusted side
    rusted_side = x

    # return the result
    result = rusted_side
    return result

print(solution())