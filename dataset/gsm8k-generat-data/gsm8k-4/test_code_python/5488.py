def solution():
    """The population of Delaware is 974,000. A study showed that there are 673 cell phones per 1000 people in the state. How many cell phones are there in Delaware?"""
    # Define the population of Delaware and the number of cell phones per 1000 people
    delaware_population = 974000
    cellphones_per_thousand = 673

    # Calculate the total number of cell phones in Delaware
    total_cellphones = delaware_population * cellphones_per_thousand / 1000

    # Return the result
    result = total_cellphones
    return result

print(solution())