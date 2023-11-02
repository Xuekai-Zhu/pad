def solution():
    
    pittsburg_stores = 2000
    pittsburg_hospitals = 500
    pittsburg_schools = 200
    pittsburg_police_stations = 20

    new_stores = pittsburg_stores / 2
    new_hospitals = pittsburg_hospitals * 2
    new_schools = pittsburg_schools - 50
    new_police_stations = pittsburg_police_stations + 5

    total_buildings = new_stores + new_hospitals + new_schools + new_police_stations
    result = total_buildings
    return result

print(solution())