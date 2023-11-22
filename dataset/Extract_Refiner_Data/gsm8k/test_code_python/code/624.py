def solution():
    
    # Define Adam's height and growth rate in inches per year
    ADAM_HEIGHT = 40
    ADAM_GROWTH_RATE = 2

    # Define the target height for the roller coaster
    TARGET_HEIGHT = 4

    # Calculate the number of years it will take for Adam to reach the target height
    years = (TARGET_HEIGHT - ADAM_HEIGHT) / ADAM_GROWTH_RATE

    # Display the number of years
    result = years
    return result

print(solution())