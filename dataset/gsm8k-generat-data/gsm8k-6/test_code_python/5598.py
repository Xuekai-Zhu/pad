To convert pounds to ounces, we multiply by 16.

def solution():
    # Find the number of towels Frances has
    num_towels_Frances = 24/4 

    # Find the weight of each towel
    weight_towel = 60 / (24 + num_towels_Frances)

    # Find the weight of Frances's towels in ounces
    weight_Frances = num_towels_Frances * weight_towel * 16

    result = weight_Frances
    return result

print(solution())