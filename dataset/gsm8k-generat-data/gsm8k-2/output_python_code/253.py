def solution():
    """A rectangular plot of private property is fenced in by a chain-link fence. The long sides of the plot are three times the length of the short sides. One short side of the fence is rusted from being hit by a sprinkler and needs to be replaced. If all the sides of the fence together are 640 feet long, how many feet of fence need to be replaced?"""
    total_fence_length = 640
    short_side_length = total_fence_length / 8
    long_side_length = 3 * short_side_length
    # The total fence length is the sum of two short sides and two long sides.
    # One short side needs to be replaced, so we subtract the old length and add the new length.
    fence_replaced_length = total_fence_length - short_side_length + long_side_length
    result = fence_replaced_length
    return result

print(solution())