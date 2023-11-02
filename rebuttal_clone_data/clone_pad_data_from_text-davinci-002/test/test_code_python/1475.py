def solution():
     slices_per_sandwich = 3
     desired_sandwiches = 50
     ham_available = 31
     ham_needed = desired_sandwiches * slices_per_sandwich - ham_available
     result = ham_needed
     return result

print(solution())