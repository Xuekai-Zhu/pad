def solution(today):
     days_to_port = 21
     days_in_port = 4
     days_from_port_to_warehouse = 7
     total_days = days_to_port + days_in_port + days_from_port_to_warehouse
     departure_day = today - total_days
     return departure_day

print(solution())