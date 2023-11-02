def solution():
    foam_per_pillow = 5 - 3 # Teddy uses 3 less than 5 pounds of foam material per pillow
    total_foam = 3 * 2000 # Teddy has 3 tons of foam material, which is 3 * 2000 pounds

    # Calculate the total number of pillows Teddy can make
    total_pillows = total_foam // foam_per_pillow
    result = total_pillows
    return result

print(solution())