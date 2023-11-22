def solution():
    
    total_cubes = 116
    strawberry_cubes = (total_cubes - 4) / 5
    blueberry_cubes = total_cubes - strawberry_cubes
    result = blueberry_cubes
    return result

print(solution())