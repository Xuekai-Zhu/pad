def solution():
    # Calculate the total number of gnomes in the first four houses
    total_gnomes_first_four = 3 * 4  # each of the first four houses has 3 gnomes, so 4 houses have 12 gnomes

    # Calculate the number of gnomes in the fifth house
    gnomes_fifth_house = 20 - total_gnomes_first_four  # subtract the total number of gnomes in the first four houses from the total number of gnomes on the street
    result = gnomes_fifth_house
    return result

print(solution())