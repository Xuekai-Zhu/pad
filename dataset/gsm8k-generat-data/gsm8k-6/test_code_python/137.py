def solution():
    # Calculate the total number of oversized beach towels used during the vacation
    total_towels_used = 3 * 4 * 7  # 3 families of 4 people sharing the rental for 7 days, with each person using 1 towel per day

    # Calculate the number of loads of laundry needed to wash all the towels
    loads_of_laundry = total_towels_used // 14 + 1  # Each load can hold 14 towels, so we divide by 14 and then add 1 if there is a remainder
    result = loads_of_laundry
    return result

print(solution())