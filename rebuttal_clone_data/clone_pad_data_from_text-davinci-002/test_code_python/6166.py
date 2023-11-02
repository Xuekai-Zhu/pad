def solution():
    total_strawberries = 900 * 3
    remaining_strawberries = 2/9 * total_strawberries
    eaten_strawberries = total_strawberries - remaining_strawberries
    strawberries_per_hedgehog = eaten_strawberries / 2
    result = strawberries_per_hedgehog
    return result

print(solution())