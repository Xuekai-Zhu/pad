def solution():
    total_houses = 5  # There are 5 houses on the street
    gnomes_per_house = 3  # The first four houses have 3 gnomes each
    total_gnomes = 20  # There are a total of 20 gnomes on the street

    # Calculate the number of gnomes in the first four houses
    gnomes_in_first_four_houses = total_houses * gnomes_per_house

    # Calculate the number of gnomes in the fifth house
    gnomes_in_fifth_house = total_gnomes - gnomes_in_first_four_houses
    result = gnomes_in_fifth_house
    return result

print(solution())