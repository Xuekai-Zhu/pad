def solution():
    budget = 10  # Danielle has $10 for supplies
    molds_cost = 3  # Danielle buys one set of molds for $3
    sticks_cost = 1  # Danielle buys a pack of 100 popsicle sticks for $1
    juice_cost = 2  # Each bottle of juice costs $2 and makes 20 popsicles

    # Calculate the maximum number of popsicles Danielle can make
    max_popsicles = (budget - molds_cost - sticks_cost) // juice_cost * 20

    # Calculate the number of popsicle sticks Danielle will be left with
    leftover_sticks = (budget - molds_cost - sticks_cost) % juice_cost * 100

    result = leftover_sticks
    return result

print(solution())