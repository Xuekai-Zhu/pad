def solution():
    # Define the initial number of green and blue crayons
    green_crayons = 5
    blue_crayons = 8

    # Subtract the number of crayons given to Becky
    green_crayons -= 3
    blue_crayons -= 1

    # Calculate the total number of crayons remaining
    total_crayons = green_crayons + blue_crayons
    result = total_crayons
    return result

print(solution())