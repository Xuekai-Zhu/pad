def solution():
    
    # Define the cost of each picture frame and the percentage of the cost for logo
    FRAME_COST = 20
    logo_percentage = 0.2

    # Calculate the cost of each picture frame with the logo
    picture_frame_cost = FRAME_COST * (1 + logo_percentage)

    # Calculate the total cost of the seniors' gifts
    total_cost = (4 * FRAME_COST) + 2 * 5 + (4 * 12)

    # Display the total cost
    result = total_cost
    return result

print(solution())