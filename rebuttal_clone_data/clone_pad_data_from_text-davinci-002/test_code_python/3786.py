def solution():
     current_length = 14
     desired_length = 12
     donation_length = 23
     length_needed = donation_length - current_length
     result = desired_length - length_needed
     return result

print(solution())