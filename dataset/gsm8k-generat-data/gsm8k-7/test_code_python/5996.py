def solution():
    year1_production = 40
    year2_production = 8 + 2 * year1_production
    year3_production = (3/4) * year2_production

    total_production = year1_production + year2_production + year3_production
    result = total_production
    return result

print(solution())