def solution():
    initial_c_j = 80  # John's initial Clean & Jerk weight
    initial_snatch = 50  # John's initial Snatch weight
    new_c_j = initial_c_j * 2  # John's new Clean & Jerk weight is double his initial weight
    new_snatch = initial_snatch * 1.8  # John's new Snatch weight is 80% higher than his initial weight
    combined_total = new_c_j + new_snatch  # Calculate John's new combined lifting capacity
    result = combined_total
    return result

print(solution())