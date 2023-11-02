def solution():
    """Alexander was 50 inches on his 8th birthday. If he grows 1/2 a foot a year, how many inches tall will he be on his 12th birthday?"""
    # Define the initial height in inches and the growth rate in feet per year
    initial_height = 50
    growth_rate = 0.5

    # Calculate the total growth in feet over 4 years
    total_growth_feet = growth_rate * 4

    # Convert the total growth to inches
    total_growth_inches = total_growth_feet * 12

    # Add the total growth to the initial height to get the final height
    final_height = initial_height + total_growth_inches

    # return the result
    result = final_height
    return result

print(solution())