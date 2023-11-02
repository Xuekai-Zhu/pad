def solution():
    
    # Define the growth rate of the bamboo in inches per day
    GROWTH_RATE = 30

    # Define the height of the bamboo in feet
    height_feet = 20

    # Convert the height to inches
    height_inches = 600

    # Calculate the number of days it will take to reach the height of 600 inches
    days = (height_inches - (growth_rate * 7)) / height_feet

    # Display the number of days
    result = days
    return result

print(solution())