def solution():
    pittsburg_stores = 2000
    pittsburg_hospitals = 500
    pittsburg_schools = 200
    pittsburg_police_stations = 20

    # Calculate the number of stores in the new city
    new_city_stores = pittsburg_stores / 2

    # Calculate the number of hospitals in the new city
    new_city_hospitals = pittsburg_hospitals * 2

    # Calculate the number of schools in the new city
    new_city_schools = pittsburg_schools - 50

    # Calculate the number of police stations in the new city
    new_city_police_stations = pittsburg_police_stations + 5

    # Calculate the total number of buildings required for the project
    total_buildings = new_city_stores + new_city_hospitals + new_city_schools + new_city_police_stations
    result = total_buildings
    return result

print(solution())