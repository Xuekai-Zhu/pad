def solution():
    """Matt has six cats and half of them are female. If each female cat has 7 kittens, and Matt sells 9 of them, what percentage of his remaining cats are kittens (rounded to the nearest percent)?"""
    # Calculate the number of female cats and kittens
    female_cats = 6 // 2
    kittens = female_cats * 7 - 9

    # Calculate the total number of cats remaining
    total_cats = 6 - 9/7

    # Calculate the percentage of remaining cats that are kittens
    kitten_percent = round((kittens / total_cats) * 100)

    # Display the percentage of remaining cats that are kittens
    result = kitten_percent
    return result

print(solution())