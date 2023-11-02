def solution():
    # Define the number of cruise ships
    cruise_ships = 4

    # Define the number of cargo ships as twice the number of cruise ships
    cargo_ships = 2 * cruise_ships

    # Define the number of sailboats as 6 more than the cargo ships
    sailboats = 6 + cargo_ships

    # Define the number of fishing boats as one-seventh of the number of sailboats
    fishing_boats = sailboats / 7

    # Calculate the total number of vessels
    total_vessels = cruise_ships + cargo_ships + sailboats + fishing_boats
    result = total_vessels
    return result

print(solution())