def solution():
    good_soil_acres = 60 * (2/3)  # number of acres with good soil
    clay_soil_acres = 60 * (1/3)  # number of acres with clay-rich soil
    good_soil_yield = 400  # bushels per acre on good soil
    clay_soil_yield = 200  # half as much yield per acre on clay-rich soil

    # Calculate the total bushels of corn yielded
    total_yield = (good_soil_acres * good_soil_yield) + (clay_soil_acres * clay_soil_yield)
    result = total_yield
    return result

print(solution())