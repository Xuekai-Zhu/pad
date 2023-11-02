def solution():
    """Danielle wants to make her own popsicles. She finds out she needs popsicle sticks, molds, and juice. She has $10 for supplies. She buys one set of molds for $3 and a pack of 100 popsicle sticks for $1. Each bottle of juice makes 20 popsicles and costs $2. How many popsicle sticks will she be left with if she makes as many as she can?"""
    # Define the cost of molds, popsicle sticks, and juice
    molds_cost = 3
    sticks_cost = 1
    juice_cost = 2

    # Calculate the number of popsicle sticks she can buy with her remaining money after purchasing molds and sticks
    sticks = (10 - molds_cost - sticks_cost) // sticks_cost

    # Calculate the number of popsicles she can make with the amount of juice she can buy
    popsicles = (sticks // 20) * 20

    # Calculate the number of popsicle sticks she will have left after making as many popsicles as possible
    sticks_left = sticks - popsicles

    # Return the result
    result = sticks_left
    return result

print(solution())