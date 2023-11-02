def solution():
    """Last year, Jorge planted corn on all of his 60 acres of property. Typically, corn grown on good soil yields 400 bushels per acre, but in clay-rich soil, the yield is only half as much per acre as in good soil. One-third of Jorge's 60 acres of land is clay-rich soil and the rest is good soil. How many bushels of corn did Jorge's land yield last year?"""
    total_acres = 60
    good_soil_acres = total_acres * (2/3)
    clay_soil_acres = total_acres * (1/3)
    good_soil_yield = 400
    clay_soil_yield = good_soil_yield / 2
    total_yield = (good_soil_acres * good_soil_yield) + (clay_soil_acres * clay_soil_yield)
    result = total_yield
    return result

print(solution())