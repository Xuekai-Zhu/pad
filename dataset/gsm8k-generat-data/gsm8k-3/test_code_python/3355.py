def solution():
    """A tank with a capacity of 8000 gallons is 3/4 full. Daxton empty's the tank by 40% of the total volume of water in the tank to water his vegetable farm. He then fills the tank with 30% of the volume of water remaining in the tank. Calculate the final volume of water in the tank."""
    # Calculate the current volume in the tank (3/4 full)
    current_volume = 8000 * 3/4

    # Calculate the volume of water Daxton empties from the tank
    emptied_volume = current_volume * 0.4

    # Calculate the remaining volume after Daxton empties the tank
    remaining_volume = current_volume - emptied_volume

    # Calculate the volume of water Daxton uses to fill the tank
    fill_volume = remaining_volume * 0.3

    # Calculate the final volume of water in the tank
    final_volume = remaining_volume + fill_volume

    # Display the final volume of water in the tank
    result = final_volume
    return result

print(solution())