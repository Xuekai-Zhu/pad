def solution():
    """Last year, Jorge planted corn on all of his 60 acres of property. Typically, corn grown on good soil yields 400 bushels per acre, but in clay-rich soil, the yield is only half as much per acre as in good soil. One-third of Jorge's 60 acres of land is clay-rich soil and the rest is good soil. How many bushels of corn did Jorge's land yield last year?"""
    # Define the total number of acres and the percentage of clay-rich soil
    total_acres = 60
    clay_percent = 1 / 3

    # Calculate the number of acres with good soil and clay-rich soil
    good_acres = total_acres * (1 - clay_percent)
    clay_acres = total_acres * clay_percent

    # Calculate the yield of corn in bushels per acre for good soil and clay-rich soil
    good_yield = 400
    clay_yield = good_yield / 2

    # Calculate the total yield of corn from good soil and clay-rich soil
    good_yield_total = good_acres * good_yield
    clay_yield_total = clay_acres * clay_yield
    total_yield = good_yield_total + clay_yield_total

    # return the result
    result = total_yield
    return result

print(solution())