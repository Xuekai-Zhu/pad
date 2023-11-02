def solution():
    # Calculate the initial volume of water in the tank
    initial_volume = 8000 * 3/4  # the tank is 3/4 full
    emptied_volume = initial_volume * 0.4  # Daxton empties the tank by 40% of the total volume of water in the tank
    remaining_volume = initial_volume - emptied_volume  # calculate the remaining volume of water in the tank
    filled_volume = remaining_volume * 0.3  # Daxton fills the tank with 30% of the remaining volume of water in the tank
    final_volume = remaining_volume + filled_volume  # calculate the final volume of water in the tank

    result = final_volume
    return result

print(solution())