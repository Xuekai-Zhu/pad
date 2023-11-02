def solution():
    
    
    crane_heights = [228, 120, 147]
    building_heights = [200, 100, 140]
    percent_taller = []
    
    for i in range(len(crane_heights)):
        height_difference = crane_heights[i] - building_heights[i]
        percent_taller.append((height_difference / building_heights[i]) * 100)
    
    avg_percent_taller = sum(percent_taller) / len(percent_taller)
    
    return avg_percent_taller

print(solution())