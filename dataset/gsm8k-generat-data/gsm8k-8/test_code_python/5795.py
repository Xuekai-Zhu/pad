def solution():
    # Define the total number of flowers
    total_flowers = 40

    # Calculate the number of roses
    roses = (2/5) * total_flowers

    # Calculate the number of carnations
    carnations = total_flowers - roses - 10

    result = carnations
    return result

print(solution())