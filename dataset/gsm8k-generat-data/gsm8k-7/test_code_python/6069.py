def solution():
    mia_rate = 2 * 12  # 2 dozen eggs per hour
    billy_rate = 10

    total_eggs = 170

    # Calculate the combined rate of Mia and Billy
    combined_rate = mia_rate + billy_rate

    # Calculate the time it will take to decorate all eggs
    time_required = total_eggs / combined_rate  # in hours

    result = time_required
    return result

print(solution())