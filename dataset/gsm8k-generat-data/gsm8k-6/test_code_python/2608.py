def solution():
    # Calculate the total number of slices of ham needed for 50 sandwiches
    total_ham_slices = 50 * 3  # three slices of ham in each sandwich
    ham_slices_needed = total_ham_slices - 31  # 31 slices of ham are already available
    result = ham_slices_needed
    return result

print(solution())