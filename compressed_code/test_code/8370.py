def solution():
    
    feathers_per_pound = 300
    feathers_per_pillow = feathers_per_pound * 2
    total_feathers = 3600
    pillows_stuffed = total_feathers // feathers_per_pillow
    result = pillows_stuffed
    return result

print(solution())