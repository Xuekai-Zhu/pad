def solution():
    # Define the total number of sacks of rice in the first harvest
    first_harvest = 20

    # Calculate the number of sacks of rice in the second harvest, with a twenty percent increase from the first harvest
    second_harvest = first_harvest * 1.2

    # Calculate the total number of sacks of rice in the first and second harvests
    total_harvest = first_harvest + second_harvest
    result = total_harvest
    return result

print(solution())