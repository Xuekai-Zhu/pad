def solution():
    
    # Define the number of jars and cupcakes per jar
    JARS = 6
    CUPCAKES_PER_JAR = 8

    # Calculate the total number of cupcakes needed
    total_cupcakes = JARS * CUPCAKES_PER_JAR

    # Calculate the number of pans needed
    pans_needed = total_cupcakes / 12

    # Display the number of pans needed
    result = pans_needed
    return result

print(solution())