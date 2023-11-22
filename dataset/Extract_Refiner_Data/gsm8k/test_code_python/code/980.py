def solution():
    
    # Define the length of the flower bed in feet
    bed_length = 111

    # Define the width of each flower in inches
    flower_width = 12

    # Calculate the total number of flowers needed
    total_flowers = bed_length / flower_width

    # Calculate the number of flowers that need to be filled with the remaining flowers
    remaining_flowers = total_flowers - 17

    # Calculate the total cost of the flowers
    total_cost = remaining_flowers * 6

    # Display the total cost
    result = total_cost
    return result

print(solution())