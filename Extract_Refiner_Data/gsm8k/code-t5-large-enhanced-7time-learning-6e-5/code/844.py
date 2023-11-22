def solution():
    
    # Define the number of white and floral shirts
    white_shirts = 40
    floral_shirts = 50

    # Calculate the number of white shirts with collars
    collars_white_shirts = white_shirts / 2

    # Calculate the number of floral shirts with buttons
    buttons_floral_shirts = floral_shirts - 20

    # Calculate the difference between the number of floral shirts with no buttons and white shirts with no collars
    difference = buttons_floral_shirts - collars_white_shirts

    # Display the difference
    result = difference
    return result

print(solution())