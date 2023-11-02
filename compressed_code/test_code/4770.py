def solution():
    
    total_strawberries = 3 * 900
    remaining_strawberries = total_strawberries * (2/9)
    eaten_strawberries = total_strawberries - remaining_strawberries
    strawberries_per_hedgehog = eaten_strawberries / 2
    result = strawberries_per_hedgehog
    return result

print(solution())