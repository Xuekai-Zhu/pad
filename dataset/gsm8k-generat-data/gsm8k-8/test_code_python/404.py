def solution():
    # Calculate the total bales of hay harvested this year
    total_acres = 5 + 7
    total_harvest = total_acres * 560 / 12

    # Calculate the total bales of hay needed for the horses from September to December
    total_horse_hay = 9 * 3 * (30 + 31 + 31 + 30)  # September + October + November + December

    # Calculate the bales of hay the farmer would have left by subtracting total horse hay from total harvest
    bales_left = total_harvest - total_horse_hay
    result = bales_left
    return result

print(solution())