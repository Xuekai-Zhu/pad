def solution():
    tina_pail = 4  # Tina's pail holds 4 gallons of water
    tommy_pail = tina_pail + 2  # Tommy's pail holds 2 gallons more than Tina's
    timmy_pail = tommy_pail * 2  # Timmy's pail holds twice as much as Tommy's

    trips = 3  # Each of them makes 3 trips to fill the pool
    water_filled = (tina_pail + tommy_pail + timmy_pail) * trips  # Calculate the total gallons of water filled

    result = water_filled
    return result

print(solution())