def solution():
    # Calculate the total amount of rainwater collected in the rain gauge
    total_rainwater = (4 * 2) + (3 * 3) + (0.5 * 2) + 2  # 4 inches per hour from 2pm to 4pm, 3 inches per hour from 4pm to 7pm, 0.5 inches per hour from 7pm to 9pm, and starting with 2 inches already in the rain gauge
    result = total_rainwater
    return result

print(solution())