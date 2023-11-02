def solution():
    """Danielle wants to make her own popsicles. She finds out she needs popsicle sticks, molds, and juice. She has $10 for supplies. She buys one set of molds for $3 and a pack of 100 popsicle sticks for $1. Each bottle of juice makes 20 popsicles and costs $2. How many popsicle sticks will she be left with if she makes as many as she can?"""
    supplies_budget = 10
    molds_cost = 3
    sticks_cost = 1
    total_sticks = 100
    juice_cost = 2
    popsicles_per_bottle = 20

    # Calculate the maximum number of bottles of juice she can buy
    max_juice_bottles = (supplies_budget - molds_cost - sticks_cost) // juice_cost

    # Calculate the number of popsicles she can make with the juice she bought
    max_popsicles = max_juice_bottles * popsicles_per_bottle

    # Calculate the number of popsicle sticks she'll need for the maximum number of popsicles
    sticks_per_popsicle = 1
    sticks_needed = max_popsicles * sticks_per_popsicle

    # Calculate the number of sticks she'll be left with
    sticks_left = total_sticks - sticks_needed

    result = sticks_left
    return result

print(solution())