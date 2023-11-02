def solution():
    """A tank with a capacity of 8000 gallons is 3/4 full. Daxton empty's the tank by 40% of the total volume of water in the tank to water his vegetable farm. He then fills the tank with 30% of the volume of water remaining in the tank. Calculate the final volume of water in the tank."""
    tank_capacity = 8000
    initial_volume = tank_capacity * (3/4)
    drained_volume = initial_volume * (40/100)
    remaining_volume = initial_volume - drained_volume
    filled_volume = remaining_volume * (30/100)
    final_volume = remaining_volume + filled_volume
    result = final_volume
    return result

print(solution())