def solution():
    # Calculate the total cost of land for the theater
    land_cost = 5 * (12 * 500)  # 12 square feet needed for every seat and 500 seats in total

    # Calculate the total cost of construction for the theater
    construction_cost = land_cost * 2  # construction costs twice as much as land

    # Calculate the total cost of the theater
    total_cost = land_cost + construction_cost

    # Calculate the amount covered by Tom's partner
    partner_covered = total_cost * 0.4

    # Calculate the amount Tom spends
    tom_spends = total_cost - partner_covered
    result = tom_spends
    return result

print(solution())