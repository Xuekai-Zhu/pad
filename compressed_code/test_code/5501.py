def solution():
    
    hawk_feathers = 6
    eagle_feathers = 17 * hawk_feathers
    total_feathers = hawk_feathers + eagle_feathers
    total_feathers -= 10
    remaining_feathers = total_feathers // 2
    result = remaining_feathers
    return result

print(solution())