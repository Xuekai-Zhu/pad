def solution():
     original_ratio = 10 / 17
     original_total = 189
     new_total = original_total - 10
     new_ratio = new_total / original_total
     dogs_left = new_total * new_ratio
     result = dogs_left
     return result

print(solution())