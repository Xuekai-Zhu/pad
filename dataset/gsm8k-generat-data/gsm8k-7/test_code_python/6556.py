def solution():
    total_budget = 10
    molds_price = 3
    popsicle_sticks_price = 1
    juice_price = 2
    num_popsicles_per_bottle = 20

    # Calculate the maximum number of molds Danielle can buy with her budget
    num_molds = (total_budget - popsicle_sticks_price) // molds_price

    # Calculate the maximum number of bottles of juice Danielle can buy with her budget
    num_juice_bottles = (total_budget - popsicle_sticks_price - num_molds * molds_price) // juice_price

    # Calculate the maximum number of popsicles Danielle can make
    num_popsicles = num_popsicles_per_bottle * num_juice_bottles

    # Calculate the number of popsicle sticks she'll be left with
    num_popsicle_sticks_left = (100 * num_popsicles) - (num_popsicles * num_popsicles_per_bottle)

    result = num_popsicle_sticks_left
    return result

print(solution())