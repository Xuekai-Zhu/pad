def solution():
    """Danielle wants to make her own popsicles. She finds out she needs popsicle sticks, molds, and juice. She has $10 for supplies. She buys one set of molds for $3 and a pack of 100 popsicle sticks for $1. Each bottle of juice makes 20 popsicles and costs $2. How many popsicle sticks will she be left with if she makes as many as she can?"""
    budget = 10
    molds_price = 3
    sticks_price = 1
    juice_price = 2
    total_sticks = 0
    # Calculate how many sets of molds she can buy
    molds = budget // molds_price
    budget -= molds * molds_price
    # Calculate how many popsicle sticks she can buy
    sticks = budget // sticks_price
    budget -= sticks * sticks_price
    total_sticks += sticks * 100
    # Calculate how many bottles of juice she can buy
    juice = budget // juice_price
    total_popsicles = juice * 20
    # Calculate how many popsicle sticks she needs for the popsicles
    total_sticks_needed = total_popsicles
    # Calculate the remaining popsicle sticks after making the popsicles
    remaining_sticks = total_sticks - total_sticks_needed
    result = remaining_sticks
    return result

print(solution())