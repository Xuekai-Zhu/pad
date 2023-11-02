def solution():
     total_tables = 15
     total_seats = total_tables * 10
     usually_taken_seats = total_seats - (total_seats / 10)
     result = usually_taken_seats
     return result

print(solution())