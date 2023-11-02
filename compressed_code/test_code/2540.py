def solution():
    
    feathers_per_pound = 300
    goose_feathers = 3600
    total_feathers = goose_feathers
    total_pillow_feathers = 2 * feathers_per_pound
    pillows = total_feathers // total_pillow_feathers
    result = pillows
    return result

print(solution())