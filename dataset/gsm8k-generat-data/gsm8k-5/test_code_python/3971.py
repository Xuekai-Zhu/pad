def solution():
    total_distance = 30  # Mona needs to bike a total of 30 miles in a week
    wed_distance = 12  # Mona biked 12 miles on Wednesday
    sat_distance = 2 * mon_distance  # Mona biked twice as far on Saturday as on Monday

    # Using the equation total_distance = mon_distance + wed_distance + sat_distance
    mon_distance = (total_distance - wed_distance - sat_distance)

    result = mon_distance
    return result

print(solution())