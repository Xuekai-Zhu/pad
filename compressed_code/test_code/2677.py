def solution():
    
    total_people = 40
    bicycles = round(total_people * 0.6) 
    tricycles = total_people - bicycles
    bicycle_wheels = bicycles * 2
    tricycle_wheels = tricycles * 3
    total_wheels = bicycle_wheels + tricycle_wheels
    result = total_wheels
    return result

print(solution())