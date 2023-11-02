def solution():
    """Amber is trying to decide if she wants to spend her $7 on candy or chips. She decides to buy the thing that she can get the most of. The bags of candy cost $1 and contain 12 ounces each. The bags of chips are $1.40 and contain 17 ounces each. How many ounces does she get if she buys the item that gives her the most?"""
    # Calculate the number of bags of candy she can buy
    candy_bags = 7 // 1
    candy_ounces = candy_bags * 12

    # Calculate the number of bags of chips she can buy
    chips_bags = 7 // 1.4
    chips_ounces = chips_bags * 17

    # Determine which item gives her the most ounces
    if candy_ounces > chips_ounces:
        result = candy_ounces
    else:
        result = chips_ounces
    return result

print(solution())