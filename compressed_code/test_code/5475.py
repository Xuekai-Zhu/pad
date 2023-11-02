def solution():
    
    total_pencils = 150 + 30
    containers = 5
    pencils_per_container = total_pencils // containers
    remaining_pencils = total_pencils % containers
    result = pencils_per_container
    return result

print(solution())