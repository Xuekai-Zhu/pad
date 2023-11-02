def solution():
    # Convert tons of foam material to pounds
    foam_material = 3 * 2000  # 1 ton = 2000 pounds

    # Calculate the number of pillows Teddy can make
    pillows = foam_material // (5 - 3)  # Teddy uses 3 less than 5 pounds of foam material to make each pillow
    result = pillows
    return result

print(solution())