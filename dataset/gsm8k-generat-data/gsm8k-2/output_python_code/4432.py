def solution():
    """There is a playground that is surrounded by a square fence that has a side length of 27 yards. There is a 12 yard by 9 yard garden that has fencing around it. How many yards of fencing do the playground and garden have together?"""
    playground_fence = 4 * 27
    garden_fence = 2 * (12 + 9) + 4 * 9
    total_fence = playground_fence + garden_fence
    result = total_fence
    return result

print(solution())