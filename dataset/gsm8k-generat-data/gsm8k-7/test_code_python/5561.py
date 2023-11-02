def solution():
    island_1_miles = 20
    island_2_miles = 20
    island_3_miles = 25
    island_4_miles = 25
    days_per_island = 1.5

    # Calculate the total miles walked on island 1 and 2
    total_miles_1_2 = (island_1_miles + island_2_miles) * days_per_island

    # Calculate the total miles walked on island 3 and 4
    total_miles_3_4 = (island_3_miles + island_4_miles) * days_per_island

    # Calculate the total miles walked on all islands
    total_miles = total_miles_1_2 + total_miles_3_4
    result = total_miles
    return result

print(solution())