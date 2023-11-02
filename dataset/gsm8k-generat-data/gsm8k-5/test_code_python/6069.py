def solution():
    mia_rate = 2 * 12  # Mia can decorate 2 dozen (24) eggs per hour
    billy_rate = 10  # Billy can decorate 10 eggs per hour
    total_eggs = 170  # They need to decorate 170 eggs in total

    # Calculate the time it would take them to decorate all the eggs if they worked separately
    mia_time = total_eggs / mia_rate
    billy_time = total_eggs / billy_rate

    # Calculate the time it would take them to decorate all the eggs if they worked together
    combined_rate = mia_rate + billy_rate
    combined_time = total_eggs / combined_rate

    result = combined_time
    return result

print(solution())