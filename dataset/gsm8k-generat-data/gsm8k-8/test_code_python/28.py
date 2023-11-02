def solution():
    # Define the total number of gnomes
    total_gnomes = 20

    # Calculate the number of gnomes in the first four houses
    first_four_gnomes = 4 * 3

    # Calculate the number of gnomes in the fifth house
    fifth_gnomes = total_gnomes - first_four_gnomes

    result = fifth_gnomes
    return result

print(solution())