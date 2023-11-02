def solution():
    cargo_ships = 4 * 2  # There are twice as many cargo ships as cruise ships
    sailboats = cargo_ships + 6  # There are 6 more sailboats than cargo ships
    fishing_boats = sailboats / 7  # There are seven times more fishing boats than sailboats

    # Calculate the total number of vessels on the water
    total_vessels = cargo_ships + sailboats + fishing_boats + 4  # There are 4 cruise ships

    result = total_vessels
    return result

print(solution())