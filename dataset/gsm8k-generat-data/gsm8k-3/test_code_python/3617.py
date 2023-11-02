def solution():
    """Melanie has twice as many cats as Annie, and Annie has three times fewer cats than Jacob. If Jacob has 90 cats, how many cats does Melanie have?"""
    # Define the number of cats Jacob has
    jacob_cats = 90

    # Calculate the number of cats Annie has
    annie_cats = jacob_cats // 3

    # Calculate the number of cats Melanie has
    melanie_cats = annie_cats * 2

    # Display the number of cats Melanie has
    result = melanie_cats
    return result

print(solution())