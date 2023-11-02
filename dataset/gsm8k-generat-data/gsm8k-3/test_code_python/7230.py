def solution():
    """Mitch is baking a cake and needs 3 cups of flour and two cups of sugar. He doesn't have a one cup scoop, only a 1/3 cup scoop. How many total scoops will he need?"""
    # Define the amount of flour and sugar needed in cups
    flour_needed = 3
    sugar_needed = 2

    # Calculate the number of scoops needed for flour and sugar
    flour_scoops = flour_needed * 3  # 1 cup = 3 scoops
    sugar_scoops = sugar_needed * 3  # 1 cup = 3 scoops

    # Calculate the total number of scoops needed
    total_scoops = flour_scoops + sugar_scoops

    # Display the total number of scoops needed
    result = total_scoops
    return result

print(solution())