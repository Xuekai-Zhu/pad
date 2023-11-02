def solution():
    # Calculate the banana production on the nearby island
    nearby_production = 9000

    # Calculate the banana production on Jakies Island
    jakies_production = 10 * nearby_production

    # Calculate the total banana production
    total_production = nearby_production + jakies_production
    result = total_production
    return result

print(solution())