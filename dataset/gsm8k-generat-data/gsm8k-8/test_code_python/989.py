def solution():
    # Define the amount of water Caleb and Cynthia can add each trip
    caleb_gallons = 7
    cynthia_gallons = 8

    # Define the total amount of water needed to fill the pool
    total_gallons_needed = 105

    # Calculate the number of trips needed for each person
    caleb_trips = total_gallons_needed / caleb_gallons
    cynthia_trips = total_gallons_needed / cynthia_gallons

    # Round up the number of trips to the nearest whole number and return
    result = int(math.ceil(max(caleb_trips, cynthia_trips)))
    return result

print(solution())