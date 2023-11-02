def solution():
    # Calculate the number of cargo ships
    cargo_ships = 4 * 2  # twice as many cargo ships as cruise ships

    # Calculate the number of sailboats
    fishing_boats = cargo_ships // 7  # 7 times fewer fishing boats than sailboats
    sailboats = cargo_ships + 6 + fishing_boats

    # Calculate the total number of vessels
    total_vessels = cargo_ships + sailboats + 4  # add the 4 cruise ships

    result = total_vessels
    return result

print(solution())