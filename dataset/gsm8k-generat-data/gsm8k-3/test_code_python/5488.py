def solution():
    """The population of Delaware is 974,000. A study showed that there are 673 cell phones per 1000 people in the state. How many cell phones are there in Delaware?"""
    # Define the population of Delaware
    population = 974000

    # Calculate the number of cell phones in Delaware
    cell_phones = (673/1000) * population

    # Display the number of cell phones in Delaware
    result = cell_phones
    return result

print(solution())