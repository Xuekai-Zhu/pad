def solution():
    """Alexander was 50 inches on his 8th birthday. If he grows 1/2 a foot a year, how many inches tall will he be on his 12th birthday?"""
    current_height = 50
    growth_rate = 0.5   # in feet per year
    years = 12 - 8     # years from 8th to 12th birthday
    total_growth = growth_rate * years
    final_height = current_height + (total_growth * 12)  # convert feet to inches
    result = final_height
    return result

print(solution())