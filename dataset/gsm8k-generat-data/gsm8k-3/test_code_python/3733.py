def solution():
    """Last year, Jorge planted corn on all of his 60 acres of property. 
    Typically, corn grown on good soil yields 400 bushels per acre, but in clay-rich 
    soil, the yield is only half as much per acre as in good soil. One-third of 
    Jorge's 60 acres of land is clay-rich soil and the rest is good soil. 
    How many bushels of corn did Jorge's land yield last year?"""
    # Define the yield per acre on good soil and clay-rich soil
    GOOD_SOIL_YIELD = 400
    CLAY_RICH_SOIL_YIELD = GOOD_SOIL_YIELD / 2

    # Calculate the number of acres of good soil and clay-rich soil
    good_soil_acres = 40
    clay_rich_soil_acres = 20

    # Calculate the total yield on good soil
    good_soil_yield = good_soil_acres * GOOD_SOIL_YIELD

    # Calculate the total yield on clay-rich soil
    clay_rich_soil_yield = clay_rich_soil_acres * CLAY_RICH_SOIL_YIELD

    # Calculate the total yield on all of the land
    total_yield = good_soil_yield + clay_rich_soil_yield

    # Display the total yield
    result = total_yield
    return result

print(solution())