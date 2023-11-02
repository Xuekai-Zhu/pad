def solution():
    pencils_with_eraser_sold = 200
    regular_pencils_sold = 40
    short_pencils_sold = 35
    cost_per_pencil_with_eraser = 0.8
    cost_per_regular_pencil = 0.5
    cost_per_short_pencil = 0.4
    total_sales = (pencils_with_eraser_sold * cost_per_pencil_with_eraser) + (regular_pencils_sold * cost_per_regular_pencil) + (short_pencils_sold * cost_per_short_pencil)
    result = total_sales
    return result

print(solution())