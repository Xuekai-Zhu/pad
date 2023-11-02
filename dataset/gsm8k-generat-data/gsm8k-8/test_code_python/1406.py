def solution():
    # Define the number of double-counted toddlers and the number of missed toddlers
    double_counted = 8
    missed = 3

    # Calculate the adjusted count by subtracting the double-counted and adding the missed
    adjusted_count = 26 - double_counted + missed
    result = adjusted_count
    return result

print(solution())