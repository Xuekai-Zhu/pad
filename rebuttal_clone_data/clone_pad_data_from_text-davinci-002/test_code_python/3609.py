def solution():
     columns_per_bus = 4
     rows_per_bus = 10
     buses = 6
     seats_per_bus = columns_per_bus * rows_per_bus
     total_seats = buses * seats_per_bus
     result = total_seats
     return result

print(solution())