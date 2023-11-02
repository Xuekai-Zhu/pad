def solution():
    """There are 5 houses on a street, and each of the first four houses has 3 gnomes in the garden. If there are a total of 20 gnomes on the street, how many gnomes does the fifth house have?"""
    houses = 5
    gnomes_per_house = 3
    total_gnomes = 20
    gnomes_in_fifth_house = total_gnomes - (houses - 1) * gnomes_per_house
    result = gnomes_in_fifth_house
    return result

print(solution())