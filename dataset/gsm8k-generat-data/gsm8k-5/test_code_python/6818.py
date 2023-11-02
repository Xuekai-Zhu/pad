def solution():
    scouts = 15  # Ron is hosting a camp out for 15 scouts
    smores_per_scout = 2  # Ron wants each scout to have 2 s'mores
    chocolate_sections_per_smores = 3  # Each s'more requires 3 sections of chocolate
    chocolate_bar_cost = 1.5  # Each chocolate bar costs $1.50

    # Calculate the total number of chocolate sections needed
    total_chocolate_sections = scouts * smores_per_scout * chocolate_sections_per_smores

    # Calculate the total number of chocolate bars needed
    total_chocolate_bars = total_chocolate_sections / 3

    # Calculate the total cost of the chocolate bars
    total_cost = total_chocolate_bars * chocolate_bar_cost
    result = total_cost
    return result

print(solution())