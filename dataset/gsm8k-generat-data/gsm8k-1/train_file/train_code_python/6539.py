def solution():
    """Annie calculated she has three times more toys than Mike, and two less than Tom. Mike has 6 toys. How many toys do Annie, Mike, and Tom have in total?"""
    mike_toys = 6
    annie_toys = 3 * mike_toys
    tom_toys = annie_toys + 2
    total_toys = mike_toys + annie_toys + tom_toys
    result = total_toys
    return result

print(solution())