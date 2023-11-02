def solution():
    # Calculate the total number of dots needed
    total_dots = 20 * 100

    # Calculate the total amount of dye needed in ml
    total_dye_ml = total_dots * 10

    # Calculate the total number of 400-ml bottles needed
    total_bottles = total_dye_ml // 400 + 1

    result = total_bottles
    return result

print(solution())