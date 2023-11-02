def solution():
    """There are 8 red pens in Maria's desk drawer. There are 10 more black pens than red pens. There are also 7 more blue pens than red pens. How many pens are there in all?"""
    # Define the initial number of red pens
    red_pens = 8

    # Calculate the number of black pens
    black_pens = red_pens + 10

    # Calculate the number of blue pens
    blue_pens = red_pens + 7

    # Calculate the total number of pens
    total_pens = red_pens + black_pens + blue_pens

    # return the result
    result = total_pens
    return result

print(solution())