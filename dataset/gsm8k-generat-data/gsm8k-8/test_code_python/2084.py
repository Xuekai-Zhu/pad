def solution():
    # Calculate the number of wheels on each item in the garage
    car_wheels = 4 * 2
    riding_lawnmower_wheels = 4
    timmy_bicycle_wheels = 2
    parent_bicycle_wheels = 2 * 2
    joey_tricycle_wheels = 3
    dad_unicycle_wheels = 1

    # Calculate the total number of wheels in the garage
    total_wheels = car_wheels + riding_lawnmower_wheels + timmy_bicycle_wheels + parent_bicycle_wheels + joey_tricycle_wheels + dad_unicycle_wheels
    result = total_wheels
    return result

print(solution())