def solution():
    # Define the amount of flour and sugar needed in cups
    flour = 3
    sugar = 2

    # Calculate the number of scoops needed for flour and sugar separately
    flour_scoops = flour / (1/3)
    sugar_scoops = sugar / (1/3)

    # Calculate the total number of scoops needed by adding the two amounts
    total_scoops = flour_scoops + sugar_scoops
    result = total_scoops
    return result

print(solution())