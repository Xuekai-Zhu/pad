def solution():
    
    # Define the number of pieces of bologna thrown at each red and yellow balloon
    RED_BALLOONS = 2
    YELLOW_BALLOONS = 3

    # Define the total number of pieces of bologna thrown
    total_bologna = 58

    # Calculate the number of red balloons
    red_balloons = 20

    # Calculate the number of yellow balloons
    yellow_balloons = total_bologna - red_balloons

    # Display the number of yellow balloons
    result = yellow_balloons
    return result

print(solution())