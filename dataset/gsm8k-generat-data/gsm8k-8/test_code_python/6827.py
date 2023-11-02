def solution():
    # Calculate the number of cranberries harvested by humans
    harvested_cranberries = 0.4 * 60000

    # Calculate the number of cranberries eaten by elk
    elk_cranberries = 20000

    # Calculate the number of cranberries left
    total_cranberries = 60000
    left_cranberries = total_cranberries - harvested_cranberries - elk_cranberries

    result = left_cranberries
    return result

print(solution())