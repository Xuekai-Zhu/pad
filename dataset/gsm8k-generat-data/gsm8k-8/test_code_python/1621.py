def solution():
    # Define the number of eggs in each breakfast plate
    eggs_per_plate = 2

    # Define the ratio of bacon strips to eggs
    bacon_to_eggs_ratio = 2

    # Calculate the total number of eggs needed
    total_eggs = eggs_per_plate * 14

    # Calculate the total number of bacon strips needed
    total_bacon = bacon_to_eggs_ratio * total_eggs

    result = total_bacon
    return result

print(solution())