def solution():
    # Calculate the cost of the molds and popsicle sticks
    mold_cost = 3
    stick_cost = 1
    supply_budget = 10
    juice_cost = supply_budget - mold_cost - stick_cost

    # Calculate the number of popsicles she can make with the juice
    juice_popsicles = juice_cost / 2 * 20

    # Calculate the number of sticks needed for those popsicles
    sticks_needed = juice_popsicles

    # Calculate the number of sticks she will have left after making popsicles
    sticks_left = 100 - sticks_needed
    result = sticks_left
    return result

print(solution())