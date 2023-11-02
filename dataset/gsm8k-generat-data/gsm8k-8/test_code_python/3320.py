def solution():
    # Calculate the number of tomato plants
    tomato_plants = 3 * 5

    # Calculate the number of cucumber plants
    cucumber_plants = 5 * 4

    # Calculate the total number of plants already in the garden
    total_plants = tomato_plants + cucumber_plants + 30

    # Calculate the total number of spaces in the garden
    total_spaces = 10 * 15

    # Calculate the number of additional spaces available for planting
    additional_spaces = total_spaces - total_plants

    result = additional_spaces
    return result

print(solution())