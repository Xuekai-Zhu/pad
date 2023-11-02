def solution():
    nearby_island_production = 9000  # Banana production on the nearby island
    jakies_island_production = 10 * nearby_island_production  # Banana production on Jakies Island, 10 times nearby island

    # Calculate the total banana produce from both islands
    total_production = nearby_island_production + jakies_island_production
    result = total_production
    return result

print(solution())