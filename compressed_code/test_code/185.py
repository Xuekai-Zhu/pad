def solution():
    
    section_g_rows = 15
    section_g_cars_per_row = 10
    section_h_rows = 20
    section_h_cars_per_row = 9
    total_g_cars = section_g_rows * section_g_cars_per_row
    total_h_cars = section_h_rows * section_h_cars_per_row
    total_cars = total_g_cars + total_h_cars
    time_spent = total_cars / 11
    result = time_spent
    return result

print(solution())