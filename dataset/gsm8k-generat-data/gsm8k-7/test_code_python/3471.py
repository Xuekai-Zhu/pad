def solution():
    foam_per_pillow = 5 - 3  # Teddy uses 3 less than 5 pounds of foam per pillow
    total_foam = 3 * 2000  # Teddy has three tons of foam, which is 3 * 2000 pounds

    # Calculate the total number of pillows that Teddy can make
    num_pillows = total_foam // foam_per_pillow
    result = num_pillows
    return result

print(solution())