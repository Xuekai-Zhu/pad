def solution():
    total_house_size = 2300
    size_of_living_area = 1000
    size_of_guest_bedroom = total_house_size / 4
    size_of_master_bedroom = total_house_size - size_of_living_area - size_of_guest_bedroom
    result = size_of_master_bedroom
    
    return result

print(solution())