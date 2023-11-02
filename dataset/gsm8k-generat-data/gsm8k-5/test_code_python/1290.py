def solution():
    # Blue : Green : White = 1 : 2 : 5
    # Let's assume Andy uses 2x gallons of green paint, then he will use x gallons of blue paint and 5x gallons of white paint
    # So the total gallons of paint he uses is 2x + x + 5x = 8x
    # We know that 2x = 6 (since Andy uses 6 gallons of green paint)
    # Therefore, x = 3
    # So the total gallons of paint he uses is 2x + x + 5x = 8x = 8*3 = 24 gallons

    total_gallons = 24
    result = total_gallons
    return result

print(solution())