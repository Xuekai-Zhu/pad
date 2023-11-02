def solution():
    """There are 5 houses on a street, and each of the first four houses has 3 gnomes in the garden. If there are a total of 20 gnomes on the street, how many gnomes does the fifth house have?"""
    # Define the number of houses and gnomes per house
    num_houses = 5
    gnomes_per_house = 3

    # Calculate the total number of gnomes on the street
    total_gnomes = num_houses * gnomes_per_house

    # Calculate the number of gnomes in the fifth house
    fifth_house_gnomes = total_gnomes - (gnomes_per_house * 4)

    result = fifth_house_gnomes
    return result

print(solution())