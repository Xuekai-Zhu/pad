def solution():
    """Hannah's family has ten pigs on their farm. They also have three fewer than twice as many cows as pigs and six more goats than cows. How many animals do they have on their farm?"""
    # Define the number of pigs on the farm
    pigs = 10

    # Define the number of cows and goats
    cows = 2 * pigs - 3
    goats = cows + 6

    # Calculate the total number of animals on the farm
    total_animals = pigs + cows + goats

    # Display the total number of animals
    result = total_animals
    return result

print(solution())