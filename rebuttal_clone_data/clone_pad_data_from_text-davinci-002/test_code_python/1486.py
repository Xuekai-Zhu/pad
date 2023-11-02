def solution():
     free_haircuts = 5
     haircuts_needed = 14 - (free_haircuts % 14)
     total_haircuts = free_haircuts + haircuts_needed
     result = total_haircuts
     return result

print(solution())