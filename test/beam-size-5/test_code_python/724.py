def solution():
    
    blue_spools = 15
    dark_blue_spools = 45
    green_spools = 40
    dark_green_spools = 50
    total_spools = blue_spools + dark_blue_spools + green_spools
    percent_blue = (blue_spools / total_spools) * 100
    result = percent_blue
    return result

print(solution())