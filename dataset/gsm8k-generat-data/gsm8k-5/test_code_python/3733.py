def solution():
    good_soil_acres = 2/3 * 60  # Two-thirds of 60 acres is good soil
    clay_soil_acres = 1/3 * 60  # One-third of 60 acres is clay-rich soil

    # Calculate the total bushels of corn yielded from good soil acres
    good_soil_yield = good_soil_acres * 400

    # Calculate the total bushels of corn yielded from clay-rich soil acres
    clay_soil_yield = clay_soil_acres * 400 * 0.5

    # Calculate the total bushels of corn yielded from all acres of land
    total_yield = good_soil_yield + clay_soil_yield
    result = total_yield
    return result

print(solution())