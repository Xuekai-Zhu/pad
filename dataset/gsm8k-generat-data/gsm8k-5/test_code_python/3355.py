def solution():
    tank_capacity = 8000  # capacity of the tank is 8000 gallons
    filled_capacity = 3/4*tank_capacity  # tank is 3/4 full
    empty_capacity = 0.4*tank_capacity  # Daxton empties the tank by 40% of the total volume of water in the tank
    remaining_capacity = filled_capacity - empty_capacity  # remaining capacity
    fill_volume = 0.3*remaining_capacity  # He fills the tank with 30% of the volume of water remaining in the tank
    final_capacity = remaining_capacity + fill_volume  # Final volume of water in the tank

    result = final_capacity
    return result

print(solution())