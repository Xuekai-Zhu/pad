def solution():
    # Calculate the total number of chairs Jackson needs to buy
    chairs_for_4_seat_tables = 6 * 4  # 6 tables with 4 seats each
    chairs_for_6_seat_tables = 12 * 6  # 12 tables with 6 seats each
    total_chairs = chairs_for_4_seat_tables + chairs_for_6_seat_tables
    result = total_chairs
    return result

print(solution())