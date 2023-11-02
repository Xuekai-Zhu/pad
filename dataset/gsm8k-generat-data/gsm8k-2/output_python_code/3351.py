def solution():
    """In Sam's collection, there are ten more black pens than blue pens and twice as many blue pens as pencils. There are also eight pencils and two fewer red pens than pencils. How many pens in all are there in Sam's collection?"""
    pencils = 8
    blue_pens = 2 * pencils
    black_pens = blue_pens + 10
    red_pens = pencils - 2
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())