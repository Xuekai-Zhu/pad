def solution():
    # Define the number of weeds in each location
    flower_bed = 11
    vegetable_patch = 14
    grass = 32

    # Calculate the total number of weeds pulled
    total_weeds = flower_bed + vegetable_patch + (0.5 * grass)

    # Calculate Lucille's earnings
    earnings = total_weeds * 6

    # Subtract the cost of the soda
    remaining = earnings - 99

    result = remaining
    return result

print(solution())