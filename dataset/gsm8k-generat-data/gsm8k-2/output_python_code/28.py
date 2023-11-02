def solution():
    """There are 5 houses on a street, and each of the first four houses has 3 gnomes in the garden. If there are a total of 20 gnomes on the street, how many gnomes does the fifth house have?"""
    total_gnomes = 20
    first_four_houses = 4*3
    fifth_house_gnomes = total_gnomes - first_four_houses
    result = fifth_house_gnomes
    return result

print(solution())