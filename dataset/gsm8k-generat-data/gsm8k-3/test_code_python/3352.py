def solution():
    """In Sam's collection, there are ten more black pens than blue pens and twice as many blue pens as pencils. There are also eight pencils and two fewer red pens than pencils. How many pens in all are there in Sam's collection?"""
    # Set up equations to represent the given information
    black_pens = blue_pens + 10
    blue_pens = 2 * pencils
    red_pens = pencils - 2
    total_pens = black_pens + blue_pens + red_pens

    # Solve for the number of pens
    pencils = 8
    blue_pens = 2 * pencils
    black_pens = blue_pens + 10
    red_pens = pencils - 2
    total_pens = black_pens + blue_pens + red_pens

    # Display the total number of pens
    result = total_pens
    return result

print(solution())