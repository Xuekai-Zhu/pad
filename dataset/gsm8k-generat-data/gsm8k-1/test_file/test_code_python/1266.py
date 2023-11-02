def solution():
    """Gary bought a boat for $9000. Over the first year it depreciated 30%. The second year it depreciated another 30%. The third year it depreciated 20%. How much is the boat worth after the three years?"""
    initial_value = 9000
    year1_depreciation = 0.3
    year2_depreciation = 0.3
    year3_depreciation = 0.2
    value_after_year1 = initial_value * (1 - year1_depreciation)
    value_after_year2 = value_after_year1 * (1 - year2_depreciation)
    value_after_year3 = value_after_year2 * (1 - year3_depreciation)
    result = value_after_year3
    return result

print(solution())