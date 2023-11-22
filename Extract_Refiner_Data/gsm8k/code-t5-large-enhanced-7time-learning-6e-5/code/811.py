def solution():
    
    # Define the amount of each ingredient in the jar
    JAR_SIZE = 10

    # Calculate the amount of salt used
    salt_used = JAR_SIZE / 3

    # Calculate the amount of citrus zest used
    zest_used = salt_used / 2

    # Calculate the amount of oil used
    oil_used = salt_used * 2

    # Display the amount of oil used
    result = oil_used
    return result

print(solution())