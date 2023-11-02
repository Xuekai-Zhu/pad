def solution():
    """There are 4 wolves out hunting for the pack. The pack contains 16 additional wolves. Each wolf needs to eat 8 pounds of meat a day and the wolves won't hunt again for five days. If each deer contains 200 pounds of meat, how many deer does each wolf need to kill?"""
    
    # Define the total number of wolves
    total_wolves = 20

    # Calculate the total meat needed for 5 days
    total_meat_needed = total_wolves * 8 * 5

    # Calculate the number of deer needed to provide enough meat
    deer_needed = total_meat_needed / 200

    # Calculate the number of deer each wolf needs to kill
    deer_per_wolf = deer_needed / 4

    # Round up to the nearest whole number of deer
    deer_per_wolf = math.ceil(deer_per_wolf)

    result = deer_per_wolf
    return result

print(solution())