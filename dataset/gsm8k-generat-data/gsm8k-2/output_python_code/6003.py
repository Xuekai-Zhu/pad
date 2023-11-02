def solution():
    """It takes 50 large jelly beans to fill up a large drinking glass. It takes half that amount to fill up a small drinking glass.
    If there are 5 large drinking glasses and 3 small ones, how many jellybeans will it take to fill them up?"""
    large_glass = 50
    small_glass = large_glass / 2
    total_jellybeans = (5 * large_glass) + (3 * small_glass)
    result = total_jellybeans
    return result

print(solution())