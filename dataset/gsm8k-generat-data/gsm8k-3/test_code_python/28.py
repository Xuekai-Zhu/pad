def solution():
    """There are 5 houses on a street, and each of the first four houses has 3 gnomes in the garden. If there are a total of 20 gnomes on the street, how many gnomes does the fifth house have?"""
    # Define the total number of houses and gnomes on the street
    total_houses = 5
    total_gnomes = 20

    # Calculate the total number of gnomes in the first four houses
    first_four_gnomes = 4 * 3

    # Calculate the number of gnomes in the fifth house
    fifth_house_gnomes = total_gnomes - first_four_gnomes

    # Return the result
    result = fifth_house_gnomes
    return result

print(solution())