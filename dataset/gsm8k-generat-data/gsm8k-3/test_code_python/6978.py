def solution():
    """There are 4 wolves out hunting for the pack. The pack contains 16 additional wolves. Each wolf needs to eat 8 pounds of meat a day and the wolves won't hunt again for five days. If each deer contains 200 pounds of meat, how many deer does each wolf need to kill?"""
    # Calculate the total number of wolves
    total_wolves = 4 + 16

    # Calculate the total amount of meat needed per day
    total_meat_needed = total_wolves * 8

    # Calculate the total amount of meat needed for 5 days
    total_meat_needed *= 5

    # Calculate the number of deer needed
    deer_needed = total_meat_needed / 200

    # Calculate the number of deer each wolf needs to kill
    deer_per_wolf = deer_needed / total_wolves

    result = deer_per_wolf
    return result

print(solution())