def solution():
    # Define the initial number of baby plants
    baby_plants = 0

    # Calculate the number of baby plants produced each year
    for year in range(1, 5):
        baby_plants += 2 * 2

    result = baby_plants
    return result

print(solution())