def solution():
    initial_shells = 20  # Shara had 20 shells before vacation
    shells_found_day1 = 5  # Shara found 5 shells on the first day of vacation
    shells_found_day2 = 5  # Shara found 5 shells on the second day of vacation
    shells_found_day3 = 5  # Shara found 5 shells on the third day of vacation
    shells_found_day4 = 6  # Shara found 6 shells on the fourth day of vacation

    # Calculate the total number of shells Shara found on vacation
    total_shells_found_vacation = shells_found_day1 + shells_found_day2 + shells_found_day3 + shells_found_day4

    # Calculate Shara's total number of shells now
    total_shells = initial_shells + total_shells_found_vacation
    result = total_shells
    return result

print(solution())