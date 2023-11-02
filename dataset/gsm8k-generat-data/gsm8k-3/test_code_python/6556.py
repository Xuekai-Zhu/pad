def solution():
    """Danielle wants to make her own popsicles. She finds out she needs popsicle sticks, molds, and juice. She has $10 for supplies. She buys one set of molds for $3 and a pack of 100 popsicle sticks for $1. Each bottle of juice makes 20 popsicles and costs $2. How many popsicle sticks will she be left with if she makes as many as she can?"""
    # Define the cost of each item
    MOLD_COST = 3
    STICK_COST = 1
    JUICE_COST = 2

    # Define the number of items purchased
    num_molds = 1
    num_stick_packs = 1
    num_juice_bottles = 0
    num_popsicles = 0

    # Calculate the cost of the molds and sticks
    mold_cost = num_molds * MOLD_COST
    stick_cost = num_stick_packs * STICK_COST

    # Calculate the remaining budget after buying molds and sticks
    remaining_budget = 10 - mold_cost - stick_cost

    # Calculate the number of juice bottles that can be purchased with the remaining budget
    num_juice_bottles = remaining_budget // JUICE_COST

    # Calculate the number of popsicles that can be made with the supplies
    num_popsicles = num_juice_bottles * 20

    # Calculate the number of popsicle sticks that will be left over
    num_sticks_left = (num_stick_packs * 100) - num_popsicles

    # Display the number of popsicle sticks left
    result = num_sticks_left
    return result

print(solution())