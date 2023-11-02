def solution():
    # Calculate the number of yellow and blue chairs
    yellow_chairs = 4 * 5  # 4 times as many yellow chairs as red chairs
    blue_chairs = yellow_chairs - 2  # 2 fewer blue chairs than yellow chairs

    # Calculate the total number of chairs
    total_chairs = 5 + yellow_chairs + blue_chairs

    result = total_chairs
    return result

print(solution())