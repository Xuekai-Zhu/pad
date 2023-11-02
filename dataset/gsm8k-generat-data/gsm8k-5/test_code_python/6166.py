def solution():
    total_strawberries = 3 * 900  # There were 3 baskets, each with 900 strawberries
    remaining_strawberries = (2/9) * total_strawberries  # 2/9 of the strawberries were remaining
    eaten_strawberries = (total_strawberries - remaining_strawberries) / 2  # The hedgehogs each ate an equal number of strawberries

    result = eaten_strawberries
    return result

print(solution())