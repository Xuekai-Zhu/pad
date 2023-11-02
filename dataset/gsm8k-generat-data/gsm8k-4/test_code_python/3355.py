def solution():
    """A tank with a capacity of 8000 gallons is 3/4 full. Daxton empty's the tank by 40% of the total volume of water in the tank to water his vegetable farm. He then fills the tank with 30% of the volume of water remaining in the tank. Calculate the final volume of water in the tank."""
    # Define the initial volume of water in the tank
    initial_volume = 8000 * 0.75

    # Calculate the volume of water emptied for the vegetable farm
    emptied_volume = initial_volume * 0.4

    # Calculate the volume of water remaining in the tank
    remaining_volume = initial_volume - emptied_volume

    # Calculate the volume of water filled after emptied
    filled_volume = remaining_volume * 0.3

    # Calculate the final volume of water in the tank
    final_volume = remaining_volume + filled_volume

    # return the result
    result = final_volume
    return result

print(solution())