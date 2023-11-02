def solution():
    # Calculate the cost of popsicles sticks and molds
    molds_cost = 3
    popsicle_sticks_cost = 1
    total_mold_sticks_cost = molds_cost + popsicle_sticks_cost

    # Calculate the maximum number of juice bottles she can buy with the remaining money after buying molds and popsicle sticks
    juice_cost = 2
    remaining_money = 10 - total_mold_sticks_cost
    max_juice_bottles = remaining_money // juice_cost

    # Calculate the maximum number of popsicles she can make with the juice bottles and popsicle sticks
    popsicles_per_bottle = 20
    popsicles_per_set_of_molds = 6
    max_popsicles = max_juice_bottles * popsicles_per_bottle * popsicles_per_set_of_molds

    # Calculate the number of popsicle sticks she will be left with
    popsicle_sticks_per_popsicle = 1
    used_popsicle_sticks = max_popsicles * popsicle_sticks_per_popsicle
    left_popsicle_sticks = popsicle_sticks_cost * 100 - used_popsicle_sticks
    result = left_popsicle_sticks
    return result

print(solution())