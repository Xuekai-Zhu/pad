def solution():
    """A rectangular plot of private property is fenced in by a chain-link fence. The long sides of the plot are three times the length of the short sides. One short side of the fence is rusted from being hit by a sprinkler and needs to be replaced. If all the sides of the fence together are 640 feet long, how many feet of fence need to be replaced?"""
    total_fence_length = 640
    short_side_length = x
    long_side_length = 3*x
    perimeter = 2*short_side_length + 2*long_side_length
    x = total_fence_length / perimeter
    rusted_side_length = short_side_length
    fence_to_replace = rusted_side_length
    result = fence_to_replace
    return result

print(solution())