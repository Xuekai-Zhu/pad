def solution():
    
    # Define the initial length of Shannon's iced coffee
    initial_length = 65

    # Define the length of each ice cube in milliliters
    cube_length = 13

    # Define the length of the additional liquid in milliliters
    additional_liquid = 15

    # Calculate the length of the iced coffee
    coffee_length = initial_length + (cube_length * cube_length)

    # Calculate the length of the additional liquid in milliliters
    additional_liquid = additional_liquid * additional_liquid

    # Calculate the final length of Shannon's iced coffee
    final_length = initial_length + additional_liquid

    # Display the final length of Shannon's iced coffee
    result = final_length
    return result

print(solution())