def solution():
     total_pages_needed = 800
     pages_read_1 = 500
     pages_read_2 = 1000
     pages_left_1 = pages_read_1 - (pages_read_1 * 0.8)
     pages_left_2 = pages_read_2 - (pages_read_2 * 0.2)
     total_pages_left = pages_left_1 + pages_left_2
     result = total_pages_left 
     return result

print(solution())