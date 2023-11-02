def solution():
    # Calculate the number of apples produced in the second year
    year2_production = 8 + 2*40

    # Calculate the number of apples produced in the third year
    year3_production = 0.75*year2_production

    # Calculate the total production over three years
    total_production = 40 + year2_production + year3_production

    result = total_production
    return result

print(solution())