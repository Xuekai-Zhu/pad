def solution():
    """A tank with a capacity of 8000 gallons is 3/4 full. Daxton empty's the tank by 40% of the total volume of water in the tank to water his vegetable farm. He then fills the tank with 30% of the volume of water remaining in the tank. Calculate the final volume of water in the tank."""
    tank_capacity = 8000
    initial_volume = 0.75 * tank_capacity
    emptied_volume = 0.4 * initial_volume
    remaining_volume = initial_volume - emptied_volume
    filled_volume = 0.3*remaining_volume
    final_volume = remaining_volume + filled_volume
    result = final_volume
    return result

print(solution())