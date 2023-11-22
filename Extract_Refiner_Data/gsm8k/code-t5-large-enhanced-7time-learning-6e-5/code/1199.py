def solution():
    
    # Define Mattison's height in inches
    mattison_height = 60

    # Calculate the height of the two-story house in inches
    house_height = mattison_height * 7

    # Calculate the height of the floor to the ceiling in inches
    floor_height = house_height * 3

    # Calculate the height of the roof from the second floor's floor in inches
    roof_height = floor_height - house_height

    # Display the height of the roof from the second floor's floor in inches
    result = roof_height
    return result

print(solution())