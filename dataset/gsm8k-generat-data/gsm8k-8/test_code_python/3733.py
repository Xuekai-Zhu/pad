def solution():
    # Calculate the number of acres of clay-rich soil and good soil
    clay_acres = 60 / 3
    good_acres = 60 - clay_acres

    # Calculate the total bushels of corn from clay-rich soil
    clay_yield = 0.5 * 400 * clay_acres

    # Calculate the total bushels of corn from good soil
    good_yield = 400 * good_acres

    # Calculate the total yield from all of the land
    total_yield = clay_yield + good_yield

    result = total_yield
    return result

print(solution())