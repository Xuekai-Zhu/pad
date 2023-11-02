def solution():
    # Calculate the total number of flowers that Miriam can care for in 6 days
    total_hours = 5 * 6  # Miriam works for 6 days, 5 hours each day
    total_flowers = total_hours * 12  # Miriam can take care of 60 flowers in one day (60/5=12)
    result = total_flowers
    return result

print(solution())