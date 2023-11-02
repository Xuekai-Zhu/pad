def solution():
    total_cranberries = 60000  # Total number of cranberries in the bog
    harvested_cranberries = 0.4 * total_cranberries  # 40% of cranberries are harvested
    eaten_cranberries = 20000  # 20000 cranberries are eaten by elk

    # Calculate the remaining cranberries
    remaining_cranberries = total_cranberries - harvested_cranberries - eaten_cranberries
    result = remaining_cranberries
    return result

print(solution())