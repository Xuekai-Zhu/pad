def solution():
    feathers_per_pillow = 2
    feathers_per_pound = 300
    total_feathers = 3600
    pounds_of_feathers = total_feathers / feathers_per_pound
    pillows = pounds_of_feathers / feathers_per_pillow
    result = pillows
    return result

print(solution())