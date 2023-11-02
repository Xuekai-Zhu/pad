def solution():
    clothes_wash_time = 30
    towels_wash_time = clothes_wash_time * 2
    sheets_wash_time = towels_wash_time - 15

    # Calculate the total wash time for all clothes
    total_clothes_wash_time = clothes_wash_time * len(clothes_pile)

    # Calculate the total wash time for all towels
    total_towels_wash_time = towels_wash_time * len(towels_pile)

    # Calculate the total wash time for all sheets
    total_sheets_wash_time = sheets_wash_time * len(sheets_pile)

    # Calculate the total wash time for all items
    total_wash_time = total_clothes_wash_time + total_towels_wash_time + total_sheets_wash_time
    result = total_wash_time
    return result

print(solution())