def solution():
    
    total_cranberries = 60000
    harvested_cranberries = 0.4 * total_cranberries
    elk_eaten_cranberries = 20000
    remaining_cranberries = total_cranberries - harvested_cranberries - elk_eaten_cranberries
    result = remaining_cranberries
    return result

print(solution())