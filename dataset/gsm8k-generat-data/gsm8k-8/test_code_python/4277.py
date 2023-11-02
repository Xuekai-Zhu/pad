def solution():
    # Define the reference values
    pittsburg_stores = 2000
    pittsburg_hospitals = 500
    pittsburg_schools = 200
    pittsburg_police = 20

    # Calculate the target values
    target_stores = pittsburg_stores / 2
    target_hospitals = pittsburg_hospitals * 2
    target_schools = pittsburg_schools - 50
    target_police = pittsburg_police + 5

    # Calculate the total number of buildings needed
    total_buildings = target_stores + target_hospitals + target_schools + target_police
    result = total_buildings
    return result

print(solution())