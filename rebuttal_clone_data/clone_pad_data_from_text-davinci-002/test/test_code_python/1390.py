def solution():
     original_legos = 380
     lost_legos = 57
     given_legos = 24
     current_legos = original_legos - lost_legos - given_legos
     result = current_legos
     return result

print(solution())