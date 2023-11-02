def solution():
    num_houses = 5
    num_gnomes_per_house = 3
    total_gnomes = 20

    # Calculate the total number of gnomes in the first four houses
    total_gnomes_first_four_houses = num_houses - 1 * num_gnomes_per_house

    # Calculate the number of gnomes in the fifth house
    num_gnomes_fifth_house = total_gnomes - total_gnomes_first_four_houses

    result = num_gnomes_fifth_house
    return result

print(solution())