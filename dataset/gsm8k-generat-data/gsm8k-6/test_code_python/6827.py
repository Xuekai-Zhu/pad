def solution():
    # Calculate the number of cranberries left after harvesting and elk consumption
    harvested_cranberries = 0.4 * 60000  # 40% of the cranberries are harvested by humans
    remaining_cranberries = 60000 - harvested_cranberries - 20000  # 20000 cranberries are eaten by elk
    result = remaining_cranberries
    return result

print(solution())