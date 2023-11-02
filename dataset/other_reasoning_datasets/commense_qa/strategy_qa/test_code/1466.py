def solution():
    # Define the temperature on Triton and the materials used to make a zoot suit
    triton_temp = -235.0
    zoot_suit_material = "thin cloth"
    # Check if the temperature on Triton is below the threshold for hypothermia in humans
    if triton_temp < -40.0 and zoot_suit_material == "thin cloth":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())