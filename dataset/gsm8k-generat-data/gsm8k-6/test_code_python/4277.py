def solution():
    # Calculate the required number of stores, hospitals, schools, and police stations
    stores = 2000 / 2  # new city should have half the number of stores
    hospitals = 500 * 2  # new city should have twice as many hospitals
    schools = 200 - 50  # new city should have 50 fewer schools
    police_stations = 20 + 5  # new city should have 5 more police stations

    # Calculate the total number of buildings required
    total_buildings = stores + hospitals + schools + police_stations
    result = total_buildings
    return result

print(solution())