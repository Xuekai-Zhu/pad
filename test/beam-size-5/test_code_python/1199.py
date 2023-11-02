def solution():
    
    # Define Mattison's height
    mattison_height = 60

    # Calculate the height of the two-story house
    house_height = mattison_height * 7

    # Calculate the height of the floor on the first floor
    floor_1 = floor_1 * 3

    # Calculate the height of the floor on the second floor
    floor_2 = floor_2 * 3

    # Calculate the height of the roof from the second floor's floor
    roof_2 = floor_2 - floor_1

    # Display the height of the roof from the second floor's floor
    result = roof_2
    return result

print(solution())