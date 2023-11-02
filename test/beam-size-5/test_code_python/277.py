def solution():
    
    # Define the number of cobras and mambas in the snake park
    cobras = 40
    mambas = 60

    # Calculate the number of spots in the cobra
    cobra_spots = 70

    # Calculate the number of spots in the mambas
    mamba_spots = 2 * mambas

    # Calculate the total number of spots
    total_spots = cobra_spots + mamba_spots

    # Calculate half the number of spots they all have combined
    half_spots = total_spots / 2

    # Display half the number of spots
    result = half_spots
    return result

print(solution())