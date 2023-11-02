def solution():
    """Tim has some cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys another half the amount of soda cans he had left. If Tim has 24 cans of soda in the end, how many cans of soda did Tim have at first?"""
    # Let x be the number of cans Tim had at first
    x = 24 + 6  # Tim had 6 cans taken by Jeff, so he ended up with 24 cans at the end
    x *= 2  # Tim bought another half the amount of soda cans he had left, so he has twice the amount now
    x += 6  # Tim originally had 6 cans taken by Jeff, so we need to add those back in

    # Display the number of cans Tim had at first
    result = x
    return result

print(solution())