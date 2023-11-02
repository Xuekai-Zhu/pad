def solution():
    """Alexander was 50 inches on his 8th birthday. If he grows 1/2 a foot a year, how many inches tall will he be on his 12th birthday?"""
    starting_height = 50
    growth_per_year = 6 # 1/2 foot is 6 inches
    years = 12 - 8 # Calculate number of years from 8th to 12th birthday
    final_height = starting_height + growth_per_year * years
    result = final_height
    return result

print(solution())