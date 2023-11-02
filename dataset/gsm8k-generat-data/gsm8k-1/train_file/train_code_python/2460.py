def solution():
    """Tim's car goes down in value by $1000 a year. He bought it for $20,000. How much is it worth after 6 years?"""
    initial_value = 20000
    depreciation_per_year = 1000
    years = 6
    final_value = initial_value - (depreciation_per_year * years)
    result = final_value
    return result

print(solution())