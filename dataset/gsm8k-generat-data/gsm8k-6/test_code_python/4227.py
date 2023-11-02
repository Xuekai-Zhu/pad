def solution():
    # Calculate the total number of metal sheets needed for the fence
    total_sheets = 10 * 3  # 10 fence panels made of 3 metal sheets each

    # Calculate the total number of metal beams needed for the fence
    total_beams = 10 * 2  # 10 fence panels made of 2 metal beams each

    # Calculate the total number of metal rods needed for the sheets and beams
    total_rods = total_sheets * 10 + total_beams * 4  # Each sheet is made of 10 metal rods and each metal beam is made of 4 metal rods

    result = total_rods
    return result

print(solution())