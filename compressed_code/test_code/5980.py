def solution():
    
    section_g_rows = 15
    section_g_cars_per_row = 10
    section_h_rows = 20
    section_h_cars_per_row = 9
    total_cars = (section_g_rows * section_g_cars_per_row) + (section_h_rows * section_h_cars_per_row)
    minutes_spent = total_cars / 11
    result = minutes_spent
    return result

print(solution())