def solution():
    """In Sam's collection, there are ten more black pens than blue pens and twice as many blue pens as pencils. There are also eight pencils and two fewer red pens than pencils. How many pens in all are there in Sam's collection?"""
    # Define the initial number of pencils
    pencils = 4

    # Calculate the number of blue pens
    blue_pens = pencils * 2

    # Calculate the number of black pens
    black_pens = blue_pens + 10

    # Calculate the number of red pens
    red_pens = pencils - 2

    # Calculate the total number of pens in Sam's collection
    total_pens = blue_pens + black_pens + red_pens

    #Return the result
    result = total_pens
    return result

print(solution())