def solution():
    """Alexander was 50 inches on his 8th birthday. If he grows 1/2 a foot a year, how many inches tall will he be on his 12th birthday?"""
    # Define Alexander's initial height in inches
    initial_height_inches = 50

    # Define the growth rate in feet per year
    growth_rate_feet_per_year = 0.5

    # Calculate how many feet Alexander will have grown in 4 years
    growth_in_feet = 4 * growth_rate_feet_per_year

    # Convert the growth in feet to inches
    growth_in_inches = growth_in_feet * 12

    # Calculate Alexander's height on his 12th birthday
    height_on_12th_birthday = initial_height_inches + growth_in_inches

    # Display Alexander's height on his 12th birthday
    result = height_on_12th_birthday
    return result

print(solution())