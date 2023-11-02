def solution():
    total_harvested = 245.5
    sold_to_maxwell = 125.5
    sold_to_wilson = 78

    not_sold = total_harvested - sold_to_maxwell - sold_to_wilson
    result = not_sold
    return result

print(solution())