def solution():
    # 1 bottle = 16 ounces
    # 1 cup = 8 ounces

    recipe1 = 2 * 8  # 2 cups
    recipe2 = 1 * 8  # 1 cup
    recipe3 = 3 * 8  # 3 cups

    total_soysauce = recipe1 + recipe2 + recipe3  # total amount needed in ounces

    num_bottles = total_soysauce // 16  # round down to nearest whole bottle needed

    if total_soysauce % 16 != 0:  # if there are remaining ounces
        num_bottles += 1  # need to buy an extra bottle

    result = num_bottles
    return result

print(solution())