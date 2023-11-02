def solution():
    red_pens = 8  # Maria has 8 red pens in her drawer
    black_pens = red_pens + 10  # There are 10 more black pens than red pens
    blue_pens = red_pens + 7  # There are 7 more blue pens than red pens

    # Calculate the total number of pens in Maria's drawer
    total_pens = red_pens + black_pens + blue_pens
    result = total_pens
    return result

print(solution())