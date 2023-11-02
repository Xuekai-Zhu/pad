def solution():
    """Melanie has twice as many cats as Annie, and Annie has three times fewer cats than Jacob. If Jacob has 90 cats, how many cats does Melanie have?"""
    jacob_cats = 90
    annie_cats = jacob_cats / 3
    melanie_cats = annie_cats * 2
    result = melanie_cats
    return result

print(solution())