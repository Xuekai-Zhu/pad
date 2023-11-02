def solution():
     four_seat_tables = 6
     six_seat_tables = 12
     seats_per_four_seat_table = 4
     seats_per_six_seat_table = 6
     total_chairs = (four_seat_tables * seats_per_four_seat_table) + (six_seat_tables * seats_per_six_seat_table)
     result = total_chairs
     return result

print(solution())