def solution():
    stores = 2000  # Pittsburg has 2000 stores
    hospitals = 500  # Pittsburg has 500 hospitals
    schools = 200  # Pittsburg has 200 schools
    police_stations = 20  # Pittsburg has 20 police stations

    # New city should have half the number of stores
    new_stores = stores / 2

    # New city should have twice as many hospitals
    new_hospitals = hospitals * 2

    # New city should have 50 fewer schools
    new_schools = schools - 50

    # New city should have 5 more police stations
    new_police_stations = police_stations + 5

    # Calculate the total number of buildings required for the project
    total_buildings = new_stores + new_hospitals + new_schools + new_police_stations
    result = total_buildings
    return result

print(solution())