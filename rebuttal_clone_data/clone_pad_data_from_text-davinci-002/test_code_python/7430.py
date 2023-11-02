def solution():
     total_benches = 50
     people_per_bench = 4
     total_capacity = total_benches * people_per_bench
     people_sitting = 80
     available_spaces = total_capacity - people_sitting
     result = available_spaces
     return result

print(solution())