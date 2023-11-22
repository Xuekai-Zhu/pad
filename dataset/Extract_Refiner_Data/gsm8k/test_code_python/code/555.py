def solution():
    
    # Define the recommended daily coffee intake
    recommended_coffee = 4

    # Calculate the amount of coffee Octavia drinks
    octavia_coffee = recommended_coffee / 2

    # Calculate the amount of coffee Juan drinks
    juan_coffee = octavia_coffee * 10

    # Calculate the number of cups Juan needs to reduce his daily coffee intake
    cups_to_reduce = recommended_coffee - juan_coffee

    # Display the number of cups Juan needs to reduce his daily coffee intake
    result = cups_to_reduce
    return result

print(solution())