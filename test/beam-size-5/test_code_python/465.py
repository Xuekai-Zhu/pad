def solution():
    
    # Define the number of jars and cupcakes per jar
    jars = 6
    cupcakes_per_jar = 8

    # Calculate the total number of cupcakes
    total_cupcakes = jars * cupcakes_per_jar

    # Calculate the number of pans needed
    pans = total_cupcakes / 12

    # Display the number of pans needed
    result = pans
    return result

print(solution())