def solution():
    
    # Define the number of sheep Seattle has
    seattle_sheep = 20

    # Calculate the number of sheep Charleston has
    charleston_sheep = seattle_sheep * 4

    # Calculate the number of sheep Toulouse has
    toulouse_sheep = charleston_sheep * 2

    # Calculate the total number of sheep
    total_sheep = seattle_sheep + charleston_sheep + toulouse_sheep

    # Display the total number of sheep
    result = total_sheep
    return result

print(solution())