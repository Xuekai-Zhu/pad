def solution():
    fabian_marbles = 15
    fabian_to_kyle_ratio = 3
    fabian_to_miles_ratio = 5

    # Calculate the number of marbles that Kyle has
    kyle_marbles = fabian_marbles / (fabian_to_kyle_ratio + 1)

    # Calculate the number of marbles that Miles has
    miles_marbles = fabian_marbles / (fabian_to_miles_ratio + 1)

    # Calculate the total number of marbles that Kyle and Miles have together
    total_marbles = kyle_marbles + miles_marbles
    result = total_marbles
    return result

print(solution())