def solution():
     woodblocks_needed = 80
     woodblocks_per_log = 5
     logs_available = 8
     logs_needed = woodblocks_needed / woodblocks_per_log - logs_available
     result = logs_needed
     return result

print(solution())