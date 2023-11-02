def solution():
    # Calculate how much Alexander grows in 4 years (from 8th to 12th birthday)
    growth_in_feet = 0.5 * 4
    growth_in_inches = growth_in_feet * 12

    # Calculate Alexander's height on his 12th birthday
    height_on_12th_birthday = 50 + growth_in_inches
    result = height_on_12th_birthday
    return result

print(solution())