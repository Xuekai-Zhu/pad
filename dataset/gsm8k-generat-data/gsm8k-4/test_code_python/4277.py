def solution():
    """Jacob has been tasked with a project to write up an urban plan proposal that will be used to construct a new city. He uses Pittsburg city as a reference which has 2000 stores, 500 hospitals, 200 schools, and 20 police stations. If the new city should have half the number of stores, twice as many hospitals, 50 fewer schools, and 5 more police stations, what is the total number of buildings required for this project?"""
    # Define the reference city values
    ref_stores = 2000
    ref_hospitals = 500
    ref_schools = 200
    ref_police_stations = 20

    # Define the new city values
    new_stores = ref_stores / 2
    new_hospitals = ref_hospitals * 2
    new_schools = ref_schools - 50
    new_police_stations = ref_police_stations + 5

    # Calculate the total number of buildings required
    total_buildings = new_stores + new_hospitals + new_schools + new_police_stations

    # return the result
    result = total_buildings
    return result

print(solution())