def solution():
    """Mitch is baking a cake and needs 3 cups of flour and two cups of sugar. He doesn't have a one cup scoop, only a 1/3 cup scoop. How many total scoops will he need?"""
    # Calculate the number of scoops of flour needed
    flour_scoops = 3 / (1/3)

    # Calculate the number of scoops of sugar needed
    sugar_scoops = 2 / (1/3)

    # Calculate the total number of scoops needed
    total_scoops = flour_scoops + sugar_scoops

    # return the result
    result = total_scoops
    return result

print(solution())