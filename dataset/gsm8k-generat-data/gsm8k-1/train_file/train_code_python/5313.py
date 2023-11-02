def solution():
    """A coach placed 15 tennis balls and 5 soccer balls each into 5 baskets. He gave 5 of his students a short period of time to remove as many balls each from a basket as they could. 3 of them removed 8 balls each and the other 2 removed a certain number of balls each. If a total of 56 balls are still in the baskets, how many balls did the other 2 students each remove?"""
    total_balls = 15 + 5
    baskets = 5
    removed_by_3 = 8
    removed_by_2 = (total_balls * baskets - 3 * removed_by_3 - 56) / 2
    result = removed_by_2
    return result

print(solution())