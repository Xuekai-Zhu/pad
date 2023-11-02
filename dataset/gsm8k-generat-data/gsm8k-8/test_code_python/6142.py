def solution():
    # Calculate earnings from first floor
    first_floor_earnings = 15 * 3

    # Calculate earnings from second floor
    second_floor_earnings = 20 * 3

    # Calculate earnings from third floor (assuming only two rooms occupied)
    third_floor_earnings = 2 * (2 * 15)

    # Calculate total monthly earnings
    total_earnings = first_floor_earnings + second_floor_earnings + third_floor_earnings
    result = total_earnings
    return result

print(solution())