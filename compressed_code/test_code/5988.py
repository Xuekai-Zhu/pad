def solution():
    
    barry_reach = 5
    larry_height = 5
    larry_shoulder_height = larry_height - (larry_height * 0.2)
    combined_reach = barry_reach + larry_shoulder_height
    result = combined_reach
    return result

print(solution())