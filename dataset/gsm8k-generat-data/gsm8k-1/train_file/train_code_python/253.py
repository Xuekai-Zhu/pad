def solution():
    """Nate got lost looking for his car in the airport parking lot. He had to walk through every row in Section G and Section H to find it. Section G has 15 rows that each hold 10 cars. Section H has 20 rows that each hold 9 cars. If Nate can walk past 11 cars per minute, how many minutes did he spend searching the parking lot?"""
    section_g_rows = 15
    section_g_cars_per_row = 10
    section_h_rows = 20
    section_h_cars_per_row = 9
    total_cars = (section_g_rows * section_g_cars_per_row) + (section_h_rows * section_h_cars_per_row)
    minutes_spent = total_cars / 11
    result = minutes_spent
    return result

print(solution())