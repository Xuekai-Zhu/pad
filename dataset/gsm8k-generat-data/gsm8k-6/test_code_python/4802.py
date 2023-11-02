def solution():
    # Calculate the total amount of time Mary needs to vacuum her whole house
    total_time = 4 * (3 + 1 + 1)  # Mary has 3 bedrooms, a kitchen, and a living room, and it takes her 4 minutes to vacuum each one
    # Calculate the number of times Mary needs to charge her vacuum cleaner
    num_charges = total_time // 10 + 1 if total_time % 10 != 0 else total_time // 10  # round up to the nearest whole charge
    result = num_charges
    return result

print(solution())