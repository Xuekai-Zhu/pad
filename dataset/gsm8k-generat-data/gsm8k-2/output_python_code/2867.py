def solution():
    """There are 8 red pens in Maria's desk drawer. There are 10 more black pens than red pens. There are also 7 more blue pens than red pens. How many pens are there in all?"""
    red_pens = 8
    black_pens = red_pens + 10
    blue_pens = red_pens + 7
    total_pens = red_pens + black_pens + blue_pens
    result = total_pens
    return result

print(solution())