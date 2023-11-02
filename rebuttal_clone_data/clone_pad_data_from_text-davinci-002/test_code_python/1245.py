def solution():
    total_watermelons = 10 * 12
    watermelons_sold = total_watermelons * 0.4
    remaining_watermelons = total_watermelons - watermelons_sold
    watermelons_sold_today = remaining_watermelons / 4
    watermelons_left = remaining_watermelons - watermelons_sold_today
    result = watermelons_left
    return result

print(solution())