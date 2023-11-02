def solution():
    pittsburg_stores = 2000
    pittsburg_hospitals = 500
    pittsburg_schools = 200
    pittsburg_police = 20
    new_stores = pittsburg_stores / 2
    new_hospitals = pittsburg_hospitals * 2
    new_schools = pittsburg_schools - 50
    new_police = pittsburg_police + 5
    total_buildings = new_stores + new_hospitals + new_schools + new_police
    result = total_buildings
    return result

print(solution())