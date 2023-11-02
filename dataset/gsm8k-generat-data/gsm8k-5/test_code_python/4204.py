def solution():
    current_height = 50  # Alexander is currently 50 inches tall
    growth_rate = 0.5  # Alexander grows 1/2 a foot (6 inches) each year
    years_passed = 12 - 8  # Alexander is 8 years old now, so 4 years will pass until his 12th birthday

    # Calculate Alexander's height on his 12th birthday
    future_height = current_height + (growth_rate * 12 * years_passed)
    result = future_height
    return result

print(solution())