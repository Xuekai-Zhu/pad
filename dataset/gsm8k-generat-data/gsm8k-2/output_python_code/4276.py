def solution():
    """Jacob has been tasked with a project to write up an urban plan proposal that will be used to construct a new city. He uses Pittsburg city as a reference which has 2000 stores, 500 hospitals, 200 schools, and 20 police stations. If the new city should have half the number of stores, twice as many hospitals, 50 fewer schools, and 5 more police stations, what is the total number of buildings required for this project?"""
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