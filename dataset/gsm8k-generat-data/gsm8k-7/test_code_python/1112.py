def solution():
    total_berriers = 42
    raspberry_count = total_berriers / 2
    blackberry_count = total_berriers / 3

    blueberry_count = total_berriers - raspberry_count - blackberry_count

    result = blueberry_count
    return result

print(solution())