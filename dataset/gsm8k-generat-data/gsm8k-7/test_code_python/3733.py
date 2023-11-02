def solution():
    total_acres = 60
    good_soil_yield = 400
    clay_soil_yield = good_soil_yield / 2
    clay_soil_acres = total_acres / 3
    good_soil_acres = total_acres - clay_soil_acres

    # Calculate the yield of corn from good soil
    good_soil_yield_total = good_soil_acres * good_soil_yield

    # Calculate the yield of corn from clay soil
    clay_soil_yield_total = clay_soil_acres * clay_soil_yield

    # Calculate the total yield of corn from all acres of land
    total_yield = good_soil_yield_total + clay_soil_yield_total
    result = total_yield
    return result

print(solution())